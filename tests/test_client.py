import vcr
import pytest
import pytest_asyncio
from tap_zenefits.client import ZenefitsClient

import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
company_id = os.getenv("COMPANY_ID")

@pytest.mark.asyncio
async def test_fetch_people():
    client = ZenefitsClient(api_key)
    
    response = await client.fetch_people(company_id)
    
    person = response['data']['data'][0]

    assert response['status'] == 200
    assert 'first_name' in person
    assert 'last_name' in person
    assert 'employee_number' in person
    assert 'manager' in person
    assert 'department' in person
    assert 'title' in person
    assert 'work_email' in person
    assert 'work_phone' in person
    assert 'photo_url' in person

@pytest.mark.asyncio
async def test_fetch_employments():
    client = ZenefitsClient(api_key)

    response = await client.fetch_employments()
    
    employment = response['data']['data'][0]

    assert response['status'] == 200
    assert 'amount_type' in employment
    assert 'pay_rate' in employment
    assert 'person' in employment
    assert 'hire_date' in employment
    assert 'employment_type' in employment
    assert 'is_active' in employment
    assert 'annual_salary' in employment
    assert 'termination_date' in employment
    assert 'id' in employment

@pytest.mark.asyncio
async def test_fetch_departments():
    client = ZenefitsClient(api_key)

    response = await client.fetch_departments(company_id)
    
    department = response['data']['data'][0]

    assert response['status'] == 200
    assert 'labor_group' in department
    assert 'people' in department
    assert 'company' in department
    assert 'url' in department
    assert 'id' in department
    assert 'name' in department

@pytest.mark.asyncio
async def test_fetch_time_durations():
    client = ZenefitsClient(api_key)
        
    response = await client.fetch_time_durations()

    time_duration = response['data']['data'][0]

    assert response['status'] == 200
    assert 'is_overnight' in time_duration
    assert 'is_approved' in time_duration
    assert 'end' in time_duration
    assert 'person' in time_duration
    assert 'url' in time_duration
    assert 'approver' in time_duration
    assert 'labor_group_ids' in time_duration
    assert 'hours' in time_duration
    assert 'start' in time_duration
    assert 'state' in time_duration
    assert 'approved_datetime' in time_duration
    assert 'valid_status' in time_duration
    assert 'date' in time_duration
    assert 'activity' in time_duration
    assert 'id' in time_duration

@pytest.mark.asyncio
async def test_fetch_payruns():
    client = ZenefitsClient(api_key)
        
    response = await client.fetch_payruns()

    payrun = response['data']['data'][0]

    assert response['status'] == 200
    assert 'check_date' in payrun
    assert 'company' in payrun
    assert 'end_date' in payrun
    assert 'id' in payrun
    assert 'object' in payrun
    assert 'original_check_date' in payrun
    assert 'payrun_type' in payrun
    assert 'people' in payrun
    assert 'start_date' in payrun
    assert 'status' in payrun
    assert 'url' in payrun

@pytest.mark.asyncio
async def test_fetch_pay_stubs():
    client = ZenefitsClient(api_key)
        
    response = await client.fetch_pay_stubs()

    pay_stub = response['data']['data'][0]

    assert response['status'] == 200
    assert 'company_contributions' in pay_stub
    assert 'company_taxes' in pay_stub
    assert 'earnings' in pay_stub
    assert 'garnishments' in pay_stub
    assert 'id' in pay_stub
    assert 'object' in pay_stub
    assert 'payrun' in pay_stub
    assert 'person' in pay_stub
    assert 'person_deductions' in pay_stub
    assert 'person_taxes' in pay_stub
    assert 'summary' in pay_stub
    assert 'url' in pay_stub