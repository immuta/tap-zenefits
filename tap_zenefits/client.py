import aiohttp
import asyncio
import json

class ZenefitsClient:
    def __init__(self, api_key):
        self._client      = aiohttp.ClientSession()
        self._auth_header = {
            'Authorization': api_key
        }

    async def fetch_departments(self, company):
        url = f"https://api.zenefits.com/core/companies/{company}/departments"
        async with self._client.get(url, headers=self._auth_header) as resp:
            response = await resp.json()
        return response

    async def fetch_employments(self):
        url = "https://api.zenefits.com/core/employments"
        async with self._client.get(url, headers=self._auth_header) as resp:
            response = await resp.json()
        return response

    async def fetch_people(self, company):
        url = f"https://api.zenefits.com/core/companies/{company}/people"
        async with self._client.get(url, headers=self._auth_header) as resp:
            response = await resp.json()
        return response

    async def fetch_time_durations(self):
        url = "https://api.zenefits.com/time_attendance/time_durations"
        async with self._client.get(url, headers=self._auth_header) as resp:
            response = await resp.json()
        return response

    async def fetch_payruns(self):
        url = "https://api.zenefits.com/payroll/payruns"
        async with self._client.get(url, headers=self._auth_header) as resp:
            response = await resp.json()
        return response

    async def fetch_pay_stubs(self):
        url = "https://api.zenefits.com/payroll/payrun_pay_stubs"
        async with self._client.get(url, headers=self._auth_header) as resp:
            response = await resp.json()
        return response


