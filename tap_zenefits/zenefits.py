import aiohttp
import asyncio
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

headers = {
    'Authorization': API_KEY
}

payload = {}

async def fetch(client):
  async with client.get("http://api.zenefits.com/core/people", headers=headers, data = payload) as resp:
    # assert resp.status == 200
    return await resp.json()


async def main():
  async with aiohttp.ClientSession() as client:
    json_response = await fetch(client)
    print(json_response)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
