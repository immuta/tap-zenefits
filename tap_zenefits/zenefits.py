import aiohttp
import asyncio
import json
from dotenv import load_dotenv
import os
from collections import defaultdict
import pandas as pd
import pprint

pp = pprint.PrettyPrinter(indent=4, depth=3)

load_dotenv()
company_id = json.loads(os.getenv("dandelion_chocolate"))['company_id']
API_KEY = json.loads(os.getenv("dandelion_chocolate"))['token']

headers = {
    'Authorization': API_KEY
}


async def fetch_endpoint():
    async with aiohttp.ClientSession() as client:
        response = await fetch_people(client, company_id)
        
        return response


async def fetch_all_endpoints():
    async with aiohttp.ClientSession() as client:
        # The pay_stubs endpoint is not able to be authorized
        # pay_stubs_response = await fetch_pay_stubs(client)

        # The payruns endpoint is accessible, but the `data` is empty
        # payruns_response = await fetch_payruns(client)

        people_response = await fetch_people(client, company_id)
        employments_response = await fetch_employments(client)
        departments_response = await fetch_departments(client, company_id)
        time_durations_response = await fetch_time_durations(client)

        return people_response, employments_response, departments_response, time_durations_response


async def fetch_people(client, company):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/people", headers=headers) as resp:
        response = await resp.json()
        return response


# This endpoint is accessible, but the data field is empty. Waiting on Dandelion response.
async def fetch_payruns(client):
    async with client.get("https://api.zenefits.com/payroll/payruns", headers=headers) as resp:
        response = await resp.json()
        return response


# This endpoint is not accessible: unauthorized. The Bearer Token used is the same as other endpoints.
async def fetch_pay_stubs(client):
    async with client.get("https://api.zenefits.com/payroll/payrun_pay_stubs", headers=headers) as resp:
        response = await resp.json()
        return response


async def fetch_employments(client):
    async with client.get("https://api.zenefits.com/core/employments", headers=headers) as resp:
        response = await resp.json()
        return response


async def fetch_departments(client, company):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/departments", headers=headers) as resp:
        response = await resp.json()
        return response


async def fetch_time_durations(client):
    async with client.get("https://api.zenefits.com/time_attendance/time_durations", headers=headers) as resp:
        response = await resp.json()
        return response


loop = asyncio.get_event_loop()
api_response = loop.run_until_complete(fetch_endpoint())
data = api_response['data']['data']
data_frame = pd.DataFrame(data)
