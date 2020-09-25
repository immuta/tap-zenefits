import vcr
import pytest
import pytest_asyncio
import pytest_vcr
from tap_zenefits.zenefits import *


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


@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_fetch_departments():
    async with aiohttp.ClientSession() as client:
        response = await fetch_departments(client)

    first_response = response['data']['data'][0]

    assert response['status'] == 200
    assert 'labor_group' in first_response
    assert 'people' in first_response
    assert 'company' in first_response
    assert 'url' in first_response
    assert 'id' in first_response
    assert 'name' in first_response


@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_fetch_time_durations():
    async with aiohttp.ClientSession() as client:
        response = await fetch_time_durations(client)

    first_response = response['data']['data'][0]

    assert response['status'] == 200
    assert 'is_overnight' in first_response
    assert 'is_approved' in first_response
    assert 'end' in first_response
    assert 'person' in first_response
    assert 'url' in first_response
    assert 'approver' in first_response
    assert 'labor_group_ids' in first_response
    assert 'hours' in first_response
    assert 'start' in first_response
    assert 'state' in first_response
    assert 'approved_datetime' in first_response
    assert 'valid_status' in first_response
    assert 'date' in first_response
    assert 'activity' in first_response
    assert 'id' in first_response
