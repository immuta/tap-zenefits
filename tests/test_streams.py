import vcr
import pytest
import pytest_asyncio
from tap_zenefits.client import ZenefitsClient
from tap_zenefits.streams import *

import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
company_id = os.getenv("COMPANY_ID")
state = {}

@pytest.mark.asyncio
async def test_departments():
    client = ZenefitsClient(api_key)

    department = Departments(client, state)
    
    assert department.client == client
    assert department.tap_stream_id == 'departments'
    assert department.object_type == 'DEPARTMENT'
    assert department.key_properties == ['id']
    assert department.replication_method == 'FULL_TABLE'
    assert department.valid_replication_keys == []
    assert department.replication_key == None

@pytest.mark.asyncio
async def test_employments():
    client = ZenefitsClient(api_key)

    employment = Employments(client, state)
    
    assert employment.client == client
    assert employment.tap_stream_id == 'employments'
    assert employment.object_type == 'EMPLOYMENT'
    assert employment.key_properties == ['id']
    assert employment.replication_method == 'FULL_TABLE'
    assert employment.valid_replication_keys == []
    assert employment.replication_key == None

@pytest.mark.asyncio
async def test_pay_stubs():
    client = ZenefitsClient(api_key)

    pay_stub = PayStubs(client, state)
    
    assert pay_stub.client == client
    assert pay_stub.tap_stream_id == 'pay_stubs'
    assert pay_stub.object_type == 'PAY_STUB'
    assert pay_stub.key_properties == ['id']
    assert pay_stub.replication_method == 'FULL_TABLE'
    assert pay_stub.valid_replication_keys == []
    assert pay_stub.replication_key == None

@pytest.mark.asyncio
async def test_payruns():
    client = ZenefitsClient(api_key)

    payrun = Payruns(client, state)
    
    assert payrun.client == client
    assert payrun.tap_stream_id == 'payruns'
    assert payrun.object_type == 'PAYRUN'
    assert payrun.key_properties == ['id']
    assert payrun.replication_method == 'FULL_TABLE'
    assert payrun.valid_replication_keys == []
    assert payrun.replication_key == None

@pytest.mark.asyncio
async def test_people():
    client = ZenefitsClient(api_key)

    person = People(client, state)
    
    assert person.client == client
    assert person.tap_stream_id == 'people'
    assert person.object_type == 'PEOPLE'
    assert person.key_properties == ['id']
    assert person.replication_method == 'FULL_TABLE'
    assert person.valid_replication_keys == []
    assert person.replication_key == None

@pytest.mark.asyncio
async def test_time_durations():
    client = ZenefitsClient(api_key)

    time_duration = TimeDurations(client, state)
    
    assert time_duration.client == client
    assert time_duration.tap_stream_id == 'time_durations'
    assert time_duration.object_type == 'TIME_DURATION'
    assert time_duration.key_properties == ['id']
    assert time_duration.replication_method == 'FULL_TABLE'
    assert time_duration.valid_replication_keys == []
    assert time_duration.replication_key == None
