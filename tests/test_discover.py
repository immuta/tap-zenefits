import json
import vcr
import pytest
import pytest_asyncio
from tap_zenefits.client import ZenefitsClient
from tap_zenefits.discover import *

import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
company_id = os.getenv("COMPANY_ID")

@pytest.mark.asyncio
async def test_get_schemas():
    with open("tap_zenefits/schemas/departments.json") as file:
        departments_schema = json.load(file)
    with open("tap_zenefits/schemas/employments.json") as file:
        employments_schema = json.load(file)
    with open("tap_zenefits/schemas/pay_stubs.json") as file:
        pay_stubs_schema = json.load(file)
    with open("tap_zenefits/schemas/payruns.json") as file:
        payruns_schema = json.load(file)
    with open("tap_zenefits/schemas/people.json") as file:
        people_schema = json.load(file)
    with open("tap_zenefits/schemas/time_durations.json") as file:
        time_durations_schema = json.load(file)

    expected_schemas = {
        'departments': departments_schema,
        'employments': employments_schema,
        'pay_stubs': pay_stubs_schema,
        'payruns': payruns_schema,
        'people': people_schema,
        'time_durations': time_durations_schema
    }

    schemas, schemas_metadata = get_schemas()

    assert schemas == expected_schemas

@pytest.mark.asyncio
async def test_discover():
    # This is assuredly a bad test, but deadlines
    # This method is essentially built from tap-square discover method
    catalog = discover()

    assert len(catalog.streams) == 6
    # stream.tap_stream_id
    # stream.schema