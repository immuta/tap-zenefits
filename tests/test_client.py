import vcr
import pytest
import pytest_asyncio

import urllib.parse as urlparse
from urllib.parse import parse_qs

from tap_zenefits.client import ZenefitsClient

import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
company_id = os.getenv("COMPANY_ID")

@pytest.mark.asyncio
async def test_fetch_people():
    client = ZenefitsClient(api_key)
    
    response = client.fetch_people(company_id)
    
    person_1 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'first_name' in person_1
    assert 'last_name' in person_1
    assert 'employee_number' in person_1
    assert 'manager' in person_1
    assert 'department' in person_1
    assert 'title' in person_1
    assert 'work_email' in person_1
    assert 'work_phone' in person_1
    assert 'photo_url' in person_1

    next_url = response['data']['next_url']
    parsed_url = urlparse.urlparse(next_url)
    starting_after = parse_qs(parsed_url.query)['starting_after']

    response = client.fetch_people(company_id, starting_after)

    person_2 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'first_name' in person_2
    assert 'last_name' in person_2
    assert 'employee_number' in person_2
    assert 'manager' in person_2
    assert 'department' in person_2
    assert 'title' in person_2
    assert 'work_email' in person_2
    assert 'work_phone' in person_2
    assert 'photo_url' in person_2

    assert person_1 != person_2

@pytest.mark.asyncio
async def test_fetch_employments():
    client = ZenefitsClient(api_key)

    response = client.fetch_employments()

    employment_1 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'amount_type' in employment_1
    assert 'pay_rate' in employment_1
    assert 'person' in employment_1
    assert 'hire_date' in employment_1
    assert 'employment_type' in employment_1
    assert 'is_active' in employment_1
    assert 'annual_salary' in employment_1
    assert 'termination_date' in employment_1
    assert 'id' in employment_1

    next_url = response['data']['next_url']
    parsed_url = urlparse.urlparse(next_url)
    starting_after = parse_qs(parsed_url.query)['starting_after']

    response = client.fetch_employments(starting_after)

    employment_2 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'amount_type' in employment_2
    assert 'pay_rate' in employment_2
    assert 'person' in employment_2
    assert 'hire_date' in employment_2
    assert 'employment_type' in employment_2
    assert 'is_active' in employment_2
    assert 'annual_salary' in employment_2
    assert 'termination_date' in employment_2
    assert 'id' in employment_2

    assert employment_1 != employment_2

@pytest.mark.asyncio
async def test_fetch_departments():
    client = ZenefitsClient(api_key)

    response = client.fetch_departments(company_id)
    
    department_1 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'labor_group' in department_1
    assert 'people' in department_1
    assert 'company' in department_1
    assert 'url' in department_1
    assert 'id' in department_1
    assert 'name' in department_1

    next_url = response['data']['next_url']
    parsed_url = urlparse.urlparse(next_url)
    starting_after = parse_qs(parsed_url.query)['starting_after']

    response = client.fetch_departments(company_id, starting_after)
    
    department_2 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'labor_group' in department_2
    assert 'people' in department_2
    assert 'company' in department_2
    assert 'url' in department_2
    assert 'id' in department_2
    assert 'name' in department_2

    assert department_1 != department_2

@pytest.mark.asyncio
async def test_fetch_time_durations():
    client = ZenefitsClient(api_key)
        
    response = client.fetch_time_durations()

    time_duration_1 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'is_overnight' in time_duration_1
    assert 'is_approved' in time_duration_1
    assert 'end' in time_duration_1
    assert 'person' in time_duration_1
    assert 'url' in time_duration_1
    assert 'approver' in time_duration_1
    assert 'labor_group_ids' in time_duration_1
    assert 'hours' in time_duration_1
    assert 'start' in time_duration_1
    assert 'state' in time_duration_1
    assert 'approved_datetime' in time_duration_1
    assert 'valid_status' in time_duration_1
    assert 'date' in time_duration_1
    assert 'activity' in time_duration_1
    assert 'id' in time_duration_1

    next_url = response['data']['next_url']
    parsed_url = urlparse.urlparse(next_url)
    starting_after = parse_qs(parsed_url.query)['starting_after']

    response = client.fetch_time_durations(starting_after)

    time_duration_2 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'is_overnight' in time_duration_2
    assert 'is_approved' in time_duration_2
    assert 'end' in time_duration_2
    assert 'person' in time_duration_2
    assert 'url' in time_duration_2
    assert 'approver' in time_duration_2
    assert 'labor_group_ids' in time_duration_2
    assert 'hours' in time_duration_2
    assert 'start' in time_duration_2
    assert 'state' in time_duration_2
    assert 'approved_datetime' in time_duration_2
    assert 'valid_status' in time_duration_2
    assert 'date' in time_duration_2
    assert 'activity' in time_duration_2
    assert 'id' in time_duration_2

    assert time_duration_1 != time_duration_2

@pytest.mark.asyncio
async def test_fetch_payruns():
    client = ZenefitsClient(api_key)
        
    response = client.fetch_payruns()

    payrun_1 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'check_date' in payrun_1
    assert 'company' in payrun_1
    assert 'end_date' in payrun_1
    assert 'id' in payrun_1
    assert 'object' in payrun_1
    assert 'original_check_date' in payrun_1
    assert 'payrun_type' in payrun_1
    assert 'people' in payrun_1
    assert 'start_date' in payrun_1
    assert 'status' in payrun_1
    assert 'url' in payrun_1

    next_url = response['data']['next_url']
    parsed_url = urlparse.urlparse(next_url)
    starting_after = parse_qs(parsed_url.query)['starting_after']

    response = client.fetch_payruns(starting_after)

    payrun_2 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'check_date' in payrun_2
    assert 'company' in payrun_2
    assert 'end_date' in payrun_2
    assert 'id' in payrun_2
    assert 'object' in payrun_2
    assert 'original_check_date' in payrun_2
    assert 'payrun_type' in payrun_2
    assert 'people' in payrun_2
    assert 'start_date' in payrun_2
    assert 'status' in payrun_2
    assert 'url' in payrun_2

    assert payrun_1 != payrun_2

@pytest.mark.asyncio
async def test_fetch_pay_stubs():
    client = ZenefitsClient(api_key)
        
    response = client.fetch_pay_stubs()

    pay_stub_1 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'company_contributions' in pay_stub_1
    assert 'company_taxes' in pay_stub_1
    assert 'earnings' in pay_stub_1
    assert 'garnishments' in pay_stub_1
    assert 'id' in pay_stub_1
    assert 'object' in pay_stub_1
    assert 'payrun' in pay_stub_1
    assert 'person' in pay_stub_1
    assert 'person_deductions' in pay_stub_1
    assert 'person_taxes' in pay_stub_1
    assert 'summary' in pay_stub_1
    assert 'url' in pay_stub_1

    next_url = response['data']['next_url']
    parsed_url = urlparse.urlparse(next_url)
    starting_after = parse_qs(parsed_url.query)['starting_after']

    response = client.fetch_pay_stubs(starting_after)

    pay_stub_2 = response['data']['data'][0]

    assert response['status'] == 200
    assert 'company_contributions' in pay_stub_2
    assert 'company_taxes' in pay_stub_2
    assert 'earnings' in pay_stub_2
    assert 'garnishments' in pay_stub_2
    assert 'id' in pay_stub_2
    assert 'object' in pay_stub_2
    assert 'payrun' in pay_stub_2
    assert 'person' in pay_stub_2
    assert 'person_deductions' in pay_stub_2
    assert 'person_taxes' in pay_stub_2
    assert 'summary' in pay_stub_2
    assert 'url' in pay_stub_2

    assert pay_stub_1 != pay_stub_2
