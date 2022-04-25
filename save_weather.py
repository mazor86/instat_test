import aiohttp
import asyncio
import json

API_KEY = 'bdc7f1097e1d575e3289f352ec4d8cd9'
CITIES_ID = {
    'Tbilisi': 611717,
    'Batumi': 615532,
    'Moscow': 524894
}

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        data = await asyncio.gather(*[
            fetch(session, url)
            for url in urls
        ])
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

cities_to_fetch = [f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}'
                   for city_id in CITIES_ID.values()]

asyncio.run(fetch_all(cities_to_fetch))