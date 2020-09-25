import aiohttp
import asyncio
import json
from dotenv import load_dotenv
import os
from collections import defaultdict
from tap_zenefits.helpers_dandelion import *

load_dotenv()

companies = {
    'dandelion chocolate': '76795'
}

API_KEY = json.loads(os.getenv("API_KEYS"))["dandelion chocolate"]

headers = {
    'Authorization': API_KEY
}


async def main():
    async with aiohttp.ClientSession() as client:
        # The pay_stubs endpoint is not able to be authorized
        # pay_stubs_response = await fetch_pay_stubs(client)

        # The payruns endpoint is accessible, but the `data` is empty
        # payruns_response = await fetch_payruns(client)

        people_response = await fetch_people(client, companies['dandelion chocolate'])
        employments_response = await fetch_employments(client)
        departments_response = await fetch_departments(client, companies['dandelion chocolate'])
        time_durations_response = await fetch_time_durations(client)

        return people_response, employments_response, departments_response, time_durations_response


async def fetch_people(client, company):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/people", headers=headers) as resp:
        response = await resp.json()
        # people = people_dict(response)
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
        # employments = employments_dict(response)
        return response


async def fetch_departments(client, company):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/departments", headers=headers) as resp:
        response = await resp.json()
        # departments = departments_dict(response)
        return response


async def fetch_time_durations(client):
    async with client.get("https://api.zenefits.com/time_attendance/time_durations", headers=headers) as resp:
        response = await resp.json()
        # time_durations = time_durations_dict(response)
        return response


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
