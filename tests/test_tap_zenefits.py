import vcr
import pytest
import pytest_asyncio
import pytest_vcr
from tap_zenefits.zenefits import *

# @pytest.fixture
# async def service(endpoint):
#     async with aiohttp.ClientSession() as client:
#         return await endpoint(client)


@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_fetch_people():
    async with aiohttp.ClientSession() as client:
        response = await fetch_people(client)
    
    assert response['status'] == 200
    assert 'first_name' in response['data']['data'][0]
    assert 'last_name' in response['data']['data'][0]
    assert 'employee_number' in response['data']['data'][0]
    assert 'manager' in response['data']['data'][0]
    assert 'department' in response['data']['data'][0]
    assert 'title' in response['data']['data'][0]
    assert 'work_email' in response['data']['data'][0]
    assert 'work_phone' in response['data']['data'][0]
    assert 'photo_url' in response['data']['data'][0]


@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_fetch_employments():
    async with aiohttp.ClientSession() as client:
        response = await fetch_employments(client)
    
    assert response['status'] == 200

