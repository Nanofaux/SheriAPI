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


class SheriException(Exception):
    pass


class InvalidToken(SheriException):
    def __init__(self):
        super().__init__(
            "It looks like the provided token was invalid and the endpoint you used required an authentication token.\n"
            "   Make sure you have the correct API key, of which you can obtain by going to "
            "https://sheri.bot/settings/ and scrolling to the bottom. "
        )


class InvalidEndpoint(SheriException):
    def __init__(self, endpoint):
        super().__init__(
            f"Sorry, but it appears that the '{endpoint}' endpoint is not valid.\n"
            f"  Please check with https://sheri.bot/api/ to view all of the possible endpoints you can use."
        )


class NSFWEndpointWithoutAllowNSFW(SheriException):
    def __init__(self):
        super().__init__(
            "Sorry, but you're attempting to request data from an NSFW endpoint, and you did not explicitly allow "
            "NSFW endpoints when initializing the class.\n"
            "   If you'd like to enable NSFW endpoint fetching, please pass in 'allow_nsfw=True`. "
        )
