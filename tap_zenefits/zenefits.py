import aiohttp
import asyncio
import json
from dotenv import load_dotenv
import os
from collections import defaultdict
import pandas as pd
import pprint
import singer
from datetime import datetime, timezone
from schema_classes import People, Payruns, PayStubs, Employments, Departments, TimeDurations

person = People()
payrun = Payruns()
pay_stub = PayStubs()
employment = Employments()
department = Departments()
time_duration = TimeDurations()

pp = pprint.PrettyPrinter(indent=4, depth=3)

args = singer.utils.parse_args(["token", "company_id"])
company_id = args.config['company_id']
API_KEY = args.config['token']

# The code below is for testing with Pytest.
# load_dotenv()
# company_id = json.loads(os.getenv("dandelion_chocolate"))['company_id']
# API_KEY = json.loads(os.getenv("dandelion_chocolate"))['token']

headers = {
    'Authorization': API_KEY
}


async def fetch_endpoint(endpoint_name):
    async with aiohttp.ClientSession() as client:
        endpoints = {
            "people": await fetch_people(client, company_id),
            "payruns": await fetch_payruns(client),
            "pay_stubs": await fetch_pay_stubs(client),
            "employments": await fetch_employments(client),
            "departments": await fetch_departments(client, company_id),
            "time_durations": await fetch_time_durations(client)
        }

        try:
            return endpoints[endpoint_name]
        except KeyError:
            return "Key not found. Please enter a valid endpoint: people, payruns, pay_stubs, employments, departments, time_durations"


async def fetch_all_endpoints():
    async with aiohttp.ClientSession() as client:
        people_response = await fetch_people(client, company_id)
        employments_response = await fetch_employments(client)
        departments_response = await fetch_departments(client, company_id)
        time_durations_response = await fetch_time_durations(client)
        payruns_response = await fetch_payruns(client)
        pay_stubs_response = await fetch_pay_stubs(client)

        return people_response, employments_response, departments_response, time_durations_response, payruns_response, pay_stubs_response


async def fetch_people(client, company):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/people", headers=headers) as resp:
        response = await resp.json()

        singer.write_schema('people', person.schema, 'id')
        singer.write_records('people', response["data"]["data"])

        return response


async def fetch_payruns(client):
    async with client.get("https://api.zenefits.com/payroll/payruns", headers=headers) as resp:
        response = await resp.json()

        singer.write_schema('payruns', payrun.schema, 'id')
        singer.write_records('payruns', response["data"]["data"])

        return response


async def fetch_pay_stubs(client):
    async with client.get("https://api.zenefits.com/payroll/payrun_pay_stubs", headers=headers) as resp:
        response = await resp.json()

        singer.write_schema('pay_stubs', pay_stub.schema, 'id')
        singer.write_records('pay_stubs', response["data"]["data"])

        return response


async def fetch_employments(client):
    async with client.get("https://api.zenefits.com/core/employments", headers=headers) as resp:
        response = await resp.json()

        singer.write_schema('employments', employment.schema, 'id')
        singer.write_records('employments', response["data"]["data"])

        return response


async def fetch_departments(client, company):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/departments", headers=headers) as resp:
        response = await resp.json()

        singer.write_schema('departments', department.schema, 'id')
        singer.write_records('departments', response["data"]["data"])

        return response


async def fetch_time_durations(client):
    async with client.get("https://api.zenefits.com/time_attendance/time_durations", headers=headers) as resp:
        response = await resp.json()

        singer.write_schema('time_durations', time_duration.schema, 'id')
        singer.write_records('time_durations', response["data"]["data"])

        return response


loop = asyncio.get_event_loop()
api_response = loop.run_until_complete(fetch_all_endpoints())
