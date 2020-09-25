import vcr
import pytest
import pytest_asyncio
import pytest_vcr
from tap_zenefits.zenefits import *

# Try to find a way to reuse the ClientSession
# Maybe like: `client = aiohttp.ClientSession()`
# I'm not sure if this is possible for tests
# @pytest.fixture
# async def service(endpoint):
#     async with aiohttp.ClientSession() as client:
#         return await endpoint(client)

# Creating a class to reuse might work
# class ApiClient:
#     def __init__(self):
#         self.client = aiohttp.ClientSession()
    

# api = ApiClient()

@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_fetch_people():
    async with aiohttp.ClientSession() as client:
        response = await fetch_people(client)
    
    first_response = response['data']['data'][0]

    assert response['status'] == 200
    assert 'first_name' in first_response
    assert 'last_name' in first_response
    assert 'employee_number' in first_response
    assert 'manager' in first_response
    assert 'department' in first_response
    assert 'title' in first_response
    assert 'work_email' in first_response
    assert 'work_phone' in first_response
    assert 'photo_url' in first_response


@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_fetch_employments():
    async with aiohttp.ClientSession() as client:
        response = await fetch_employments(client)
    
    first_response = response['data']['data'][0]

    assert response['status'] == 200
    assert 'amount_type' in first_response
    assert 'pay_rate' in first_response
    assert 'person' in first_response
    assert 'hire_date' in first_response
    assert 'employment_type' in first_response
    assert 'is_active' in first_response
    assert 'annual_salary' in first_response
    assert 'termination_date' in first_response
    assert 'id' in first_response

