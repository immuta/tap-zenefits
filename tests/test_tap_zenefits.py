import vcr
import pytest
import pytest_asyncio
import pytest_vcr
from tap_zenefits.zenefits import *
from tap_zenefits.helpers_dandelion import *


@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_fetch_people():
    async with aiohttp.ClientSession() as client:
        response = await fetch_people(client, company_id)
    
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

    parsed_response = people_dict(response)
    first_parsed_response = parsed_response[first_response['id']]

    assert first_response['id'] in parsed_response
    assert 'first_name' in first_parsed_response
    assert 'last_name' in first_parsed_response
    assert 'employee_number' in first_parsed_response
    assert 'manager' in first_parsed_response
    assert 'department' in first_parsed_response
    assert 'title' in first_parsed_response
    assert 'work_email' in first_parsed_response
    assert 'work_phone' in first_parsed_response
    assert 'photo_url' in first_parsed_response


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

    parsed_response = employments_dict(response)
    first_parsed_response = parsed_response[first_response['id']]

    assert first_response['id'] in parsed_response
    assert 'amount_type' in first_parsed_response
    assert 'pay_rate' in first_parsed_response
    assert 'person' in first_parsed_response
    assert 'hire_date' in first_parsed_response
    assert 'employment_type' in first_parsed_response
    assert 'is_active' in first_parsed_response
    assert 'annual_salary' in first_parsed_response
    assert 'termination_date' in first_parsed_response
    assert 'id' in first_parsed_response


@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_fetch_departments():
    async with aiohttp.ClientSession() as client:
        response = await fetch_departments(client, company_id)

    first_response = response['data']['data'][0]

    assert response['status'] == 200
    assert 'labor_group' in first_response
    assert 'people' in first_response
    assert 'company' in first_response
    assert 'url' in first_response
    assert 'id' in first_response
    assert 'name' in first_response

    parsed_response = departments_dict(response)
    first_parsed_response = parsed_response[first_response['id']]

    assert first_response['id'] in parsed_response
    assert 'labor_group' in first_parsed_response
    assert 'people' in first_parsed_response
    assert 'company' in first_parsed_response
    assert 'url' in first_parsed_response
    assert 'id' in first_parsed_response
    assert 'name' in first_parsed_response


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

    person = first_response['person']['url'].split("people/")
    parsed_response = time_durations_dict(response)
    first_parsed_response = parsed_response[person[1]][0]

    assert person[1] in parsed_response
    assert 'is_overnight' in first_parsed_response
    assert 'is_approved' in first_parsed_response
    assert 'end' in first_parsed_response
    assert 'person' in first_parsed_response
    assert 'url' in first_parsed_response
    assert 'approver' in first_parsed_response
    assert 'labor_group_ids' in first_parsed_response
    assert 'hours' in first_parsed_response
    assert 'start' in first_parsed_response
    assert 'state' in first_parsed_response
    assert 'approved_datetime' in first_parsed_response
    assert 'valid_status' in first_parsed_response
    assert 'date' in first_parsed_response
    assert 'activity' in first_parsed_response
    assert 'id' in first_parsed_response


@pytest.mark.vcr()
def test_fetch_all_endpoints():
    response = loop.run_until_complete(fetch_all_endpoints())

    people_first_response = response[0]['data']['data'][0]

    assert response[0]['status'] == 200
    assert 'first_name' in people_first_response
    assert 'last_name' in people_first_response
    assert 'employee_number' in people_first_response
    assert 'manager' in people_first_response
    assert 'department' in people_first_response
    assert 'title' in people_first_response
    assert 'work_email' in people_first_response
    assert 'work_phone' in people_first_response
    assert 'photo_url' in people_first_response

    employments_first_response = response[1]['data']['data'][0]

    assert response[1]['status'] == 200
    assert 'amount_type' in employments_first_response
    assert 'pay_rate' in employments_first_response
    assert 'person' in employments_first_response
    assert 'hire_date' in employments_first_response
    assert 'employment_type' in employments_first_response
    assert 'is_active' in employments_first_response
    assert 'annual_salary' in employments_first_response
    assert 'termination_date' in employments_first_response
    assert 'id' in employments_first_response

    departments_first_response = response[2]['data']['data'][0]

    assert response[2]['status'] == 200
    assert 'labor_group' in departments_first_response
    assert 'people' in departments_first_response
    assert 'company' in departments_first_response
    assert 'url' in departments_first_response
    assert 'id' in departments_first_response
    assert 'name' in departments_first_response

    time_durations_first_response = response[3]['data']['data'][0]

    assert response[3]['status'] == 200
    assert 'is_overnight' in time_durations_first_response
    assert 'is_approved' in time_durations_first_response
    assert 'end' in time_durations_first_response
    assert 'person' in time_durations_first_response
    assert 'url' in time_durations_first_response
    assert 'approver' in time_durations_first_response
    assert 'labor_group_ids' in time_durations_first_response
    assert 'hours' in time_durations_first_response
    assert 'start' in time_durations_first_response
    assert 'state' in time_durations_first_response
    assert 'approved_datetime' in time_durations_first_response
    assert 'valid_status' in time_durations_first_response
    assert 'date' in time_durations_first_response
    assert 'activity' in time_durations_first_response
    assert 'id' in time_durations_first_response
