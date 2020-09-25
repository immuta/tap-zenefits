import aiohttp
import asyncio
import json
from dotenv import load_dotenv
import os
from collections import defaultdict

load_dotenv()

company = '76795'

API_KEY = os.getenv("API_KEY")

headers = {
    'Authorization': API_KEY
}


async def main():
    async with aiohttp.ClientSession() as client:
        people_response = await fetch_people(client)
        # The pay_stubs endpoint is not able to be authorized
        # pay_stubs_response = await fetch_pay_stubs(client)
        employments_response = await fetch_employments(client)
        departments_response = await fetch_departments(client)
        time_durations_response = await fetch_time_durations(client)

        return people_response, employments_response, departments_response, time_durations_response


async def fetch_people(client):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/people", headers=headers) as resp:
        response = await resp.json()
        # people = people_dict(response)
        return response


async def fetch_pay_stubs(client):
    async with client.get("https://api.zenefits.com/payroll/payrun_pay_stubs", headers=headers) as resp:
        response = await resp.json()
        return json.dumps(response)


async def fetch_employments(client):
    async with client.get("https://api.zenefits.com/core/employments", headers=headers) as resp:
        response = await resp.json()
        # employments = employments_dict(response)
        return response


async def fetch_departments(client):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/departments", headers=headers) as resp:
        response = await resp.json()
        departments = departments_dict(response)
        return departments


async def fetch_time_durations(client):
    async with client.get("https://api.zenefits.com/time_attendance/time_durations", headers=headers) as resp:
        response = await resp.json()
        time_durations = time_durations_dict(response)
        return time_durations


def people_dict(response):
    employees = {}

    for person in response['data']['data']:
        employees[person['id']] = {
            'first_name': person['first_name'],
            'last_name': person['last_name'],
            'employee_number': person['employee_number'],
            'manager': person['manager']['url'],
            'department': person['department']['url'],
            'title': person['title'],
            'work_email': person['work_email'],
            'work_phone': person['work_phone'],
            'photo_url': person['photo_url']
        }

    return json.dumps(employees)


def employments_dict(response):
    employments = {}

    for person in response['data']['data']:
        # This returns the employment id, but it could return the people id
        employments[person['id']] = person

    return json.dumps(employments)


def departments_dict(response):
    departments = {}

    for department in response['data']['data']:
        # This returns the department id
        departments[department['id']] = department

    return json.dumps(departments)


def time_durations_dict(response):
    time_durations = {}
    time_durations = defaultdict(lambda: [], time_durations)

    for duration in response['data']['data']:
        # This returns the person id, but it could return the duration id.
        # The person id has a value of a list that contains all durations
        person = duration['person']['url'].split("people/")
        time_durations[person[1]].append(duration)

    return json.dumps(time_durations)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
