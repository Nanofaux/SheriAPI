# -*- coding: utf-8 -*-

"""
The MIT License (MIT)
Copyright (c) 2021 Nanofaux
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import io
import logging
import os
import re
import sys
from types import SimpleNamespace
from typing import Union, Any, List, Optional

import aiohttp

from . import __version__
from .endpoints import nsfw_endpoints, lookup, to_enum
from .enums import _SharedEnum
from .errors import InvalidToken, InvalidEndpoint, NSFWEndpointWithoutAllowNSFW, SheriException

logger = logging.getLogger('SheriAPI')
USER_AGENT = "SheriAPI (https://github.com/Nanofaux/SheriAPI {0}) Python/{1[0]}.{1[1]} aiohttp/{2}".format(
    __version__, sys.version_info, aiohttp.__version__
)


# Major inspiration from https://github.com/Rapptz/discord.py/
class SheriAPI:
    """ Generic Sheri API handler.

    :param token: Optional token to provide, only used when accessing non-public API endpoints.
    :type token: str

    :keyword allow_nsfw: Whether to allow NSFW endpoints to be used.
    :type allow_nsfw: bool

    :param `**kwargs`:
        Parameters
        ------------------
        :keyword session:
        :type aiohttp.ClientSession:
        Optionally provide a session if needed.
        If one is provided, the class will not close the session, else it will create one for you
        and close it automatically when finished.
    """

    __slots__ = ('token', 'allow_nsfw', 'session', 'close_session')

    def __init__(self,
                 token: str = None,
                 *,
                 allow_nsfw: bool = False,
                 **kwargs: Any):
        self.token = token
        self.allow_nsfw = allow_nsfw

        session = kwargs.pop('session', None)
        self.session = session or aiohttp.ClientSession()

        # We assume to only close the session if we are not given a user-provided one.
        self.close_session = not bool(session)

    async def __aenter__(self) -> "_APIHandler":
        return _APIHandler(self.token, self.session, allow_nsfw=self.allow_nsfw)

    async def get(
            self, endpoint: Union[str, _SharedEnum], count: int = 1
    ) -> Union[List["SheriResponse"], "SheriResponse"]:
        """
        Grab an image from the API with a provided endpoint.

        :param endpoint: The endpoint to use. Can be a string of said endpoint or via an Enum.
        :type endpoint: Union[str, _SharedEnum]

        :keyword count: The amount of images to return. Max 252 (As set by the API).
        :type count: int

        :returns: A SheriResponse object, or a list thereof (depending on if the user requested 1 or more images).
        :rtype: Union[List["SheriResponse"], "SheriResponse"]
        """
        async with self as api:
            return await api.get(endpoint, count=count)

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.close_session:
            await self.session.close()

    def __str__(self) -> str:
        return repr(self)  # Idk what else to really represent lol

    def __repr__(self) -> str:
        return "<SheriAPI allow_nsfw='{0.allow_nsfw}'>".format(self)


class _APIHandler:
    API_URL = "https://sheri.bot/api"
    SERVICE_UNAVAILABLE = "https://sheri.bot/media/service-unavaliable.png"

    def __init__(
            self,
            token: str,
            session: aiohttp.ClientSession,
            *,
            allow_nsfw: bool = False
    ):
        self._token = token
        self._session = session
        self.allow_nsfw = allow_nsfw

    async def get(
            self, endpoint: Union[str, _SharedEnum], *, count: Optional[int] = 1
    ) -> Union[List["SheriResponse"], "SheriResponse"]:
        """
        Grab an image from the API with a provided endpoint.

        :param endpoint: The endpoint to use. Can be a string of said endpoint or via an Enum.
        :type endpoint: Union[str, _SharedEnum]

        :keyword count: The amount of images to return. Max 252 (As set by the API).
        :type count: Optional[int]

        :returns: A :class:`SheriResponse` object, or a list thereof
            (depending on if the user requested 1 or more images).
        :rtype: Union[List["SheriResponse"], "SheriResponse"]
        """
        if isinstance(endpoint, _SharedEnum):
            _endpoint = lookup(endpoint)
        else:
            _endpoint = str(endpoint).lower()
        if _endpoint in nsfw_endpoints and not self.allow_nsfw:
            raise NSFWEndpointWithoutAllowNSFW

        url = f"{self.API_URL}/{_endpoint}"
        headers = {"Accept": "application/json",
                   "User-Agent": USER_AGENT}
        if self._token is not None:
            headers["Authorization"] = f"Token {self._token}"

        if count > 1:
            if not (isinstance(count, int) or str(count).isdigit()):
                raise TypeError("Kwarg 'count' was provided but was not an integer/wasn't of type 'int'. ")
            if count > 252:
                logger.info('[INFO] The API only allows a max of 252 responses, so there is no need to input more.')
                count = 252
            url += f"?count={count}"

        async with self._session.get(url=url, headers=headers) as response:
            status = response.status
            if status == 200:
                json = await response.json()
            elif status in [401, 403]:
                # Documentation says it's a 403 but in testing it raises a 401 so :shrug:
                raise InvalidToken
            elif status == 404:
                raise InvalidEndpoint(endpoint)
            else:
                raise SheriException(
                    "It looks like an unexpected error occurred when fetching your requested image:\n"
                    f"Error {status}: {await response.text()}"
                )
        try:
            if isinstance(json, list):
                return [SheriResponse(endpoint, i, self._session) for i in json]
            else:
                return SheriResponse(endpoint, json, self._session)
        except KeyError:
            logger.warning('[WARN] SheriAPI returned null JSON - Is the service unavailable?')
            return SheriResponse(endpoint, {
                'url': self.SERVICE_UNAVAILABLE,
                'report_url': self.SERVICE_UNAVAILABLE
            })


# These objects below are used internally and should never be instantiated manually.
class SheriResponse:
    __slots__ = ('endpoint', 'url', 'report_url', 'author', 'source', 'session', 'image_hash')

    def __init__(
            self,
            endpoint: Union[str, _SharedEnum],
            response: dict,
            session: Optional[aiohttp.ClientSession] = None
    ):
        if not isinstance(endpoint, _SharedEnum):
            endpoint = to_enum(endpoint)
        self.endpoint = endpoint
        self.url = response.pop('url')
        self.report_url = response.pop('report_url')
        self.author = Author(response.pop('author', {}))
        self.source = response.pop('source', None)
        self.session = session
        image_hash = re.search(r'[A-Za-z0-9\-]+\.[a-z]+$', self.url)
        if image_hash is not None:
            self.image_hash = image_hash.group(0)
        else:
            self.image_hash = None

    def __getitem__(self, item):
        return getattr(self, item)

    async def read(self) -> Optional[bytes]:
        """
        Read the image data as a :class:`bytes` object.

        :returns: The raw image data, or None if there was an error in fetching the image data.
        :rtype: Optional[bytes]
        """
        if self.session is None:
            raise TypeError(
                "It doesn't look like there's a valid image to grab here. Are you sure that "
                "the service is available?"
            )
        elif self.session.closed:
            session = aiohttp.ClientSession()
            created_session = True
        else:
            session = self.session
            created_session = False
        url = self.url
        headers = {"Accept": "application/json",
                   "User-Agent": USER_AGENT}
        try:
            async with session.get(url, headers=headers) as resp:
                if resp.status == 200:
                    return await resp.read()
                else:
                    logger.warning(
                        f'[WARN] Attempted to fetch image data from {url} however the server responded '
                        f'with a {resp.status}.'
                    )
                    return None
        finally:
            if created_session:
                await session.close()

    async def save(
            self,
            fp: Union[io.BufferedIOBase, os.PathLike, str],
            *,
            seek_begin: bool = True
    ) -> int:
        """
        Save the image locally to the disk via a specified file path.

        :param fp: The optional path to save the image data to.
        :type fp: Union[io.BufferedIOBase, os.PathLike, str]

        :param seek_begin: Whether to seek to the beginning of the file after saving.
        :type seek_begin: bool

        :returns: The number of bytes written.
        :rtype: int
        """
        data = await self.read()
        if isinstance(fp, io.IOBase) and fp.writable():
            written = fp.write(data)
            if seek_begin:
                fp.seek(0)
            return written
        else:
            with open(fp, 'wb') as f:
                return f.write(data)

    def __str__(self) -> str:
        return self.url


class Author(SimpleNamespace):
    def __init__(self, data: dict) -> None:
        super().__init__(**data)

    def __str__(self) -> str:
        return self.name
