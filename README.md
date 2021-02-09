[THIS ISN'T RELEASED YET REE]

A simple API wrapper for Sheri Blossom (https://sheri.bot/)

The API provides several endpoints for free however some will require a unique token.

You can obtain your token by going to the dashboard (https://sheri.bot/settings/) and scrolling to the bottom.

Examples:

```python
from SheriAPI import SheriAPI

api = SheriAPI(token="Your Token Here")

res = await api.get('hug')

# Get the image URL
url = res.url
# Or the report URL
report_url = res.report_url

# Save the image to disk
await res.save('/')
```
You can also use it in a context manager if you like:
```python
from SheriAPI import SheriAPI

async with SheriAPI(token="Your Token Here") as api:
    img = await api.get('fox')
    img2 = await api.get('cat')
    await img.save('/foxes')
    await img2.save('/cats')
```
Additionally, there are enums of which list all applicable API endpoints. 
You may use them as well.
```python
from SheriAPI import SheriAPI, FreeEndpoint

async with SheriAPI() as api:
    img = await api.get(FreeEndpoint.Fox)
    await img.save('/foxes')
```
You can specify an amount of images to return from the API.
If it is any amount other than 1, it will be a list of SheriResponse objects.

```python
from SheriAPI import SheriAPI, FreeEndpoint

async with SheriAPI() as api:
    imgs = await api.get(
        FreeEndpoint.Fox,
        count=10
    )
    for img in imgs:
        await img.save(f"images/{img.image_hash}")
```
The only time a token is *needed* is when attempting to use an endpoint that is not free.
For example:
```python
from SheriAPI import SheriAPI, SFWEndpoint

# Works
async with SheriAPI(token="Your Token Here") as api:
    img = await api.get(SFWEndpoint.Paws)
    print(img.url)

# Raises an InvalidToken exception
async with SheriAPI() as api:
    img = await api.get(SFWEndpoint.Paws)
    print(img.url)
```

Lastly, in order to use NSFW endpoints, you must pass in `allow_nsfw=True`.
```python
from SheriAPI import SheriAPI, NSFWEndpoint

# Works
async with SheriAPI(
        token="Your Token Here",
        allow_nsfw=True
) as api:
    img = await api.get(NSFWEndpoint.Gay)
    print(img.url)

# Raises NSFWEndpointWithoutAllowNSFW exception
async with SheriAPI(token="Your Token Here") as api:
    img = await api.get(NSFWEndpoint.Dick_Wank)
    print(img.url)
```