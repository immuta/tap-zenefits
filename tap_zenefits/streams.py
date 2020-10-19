import urllib.parse as urlparse
from urllib.parse import parse_qs

import singer

LOGGER = singer.get_logger()

def get_starting_after(url):
    parsed_url   = urlparse.urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('starting_after', None)

class Stream:
    tap_stream_id          = None
    key_properties         = []
    replication_method     = ''
    valid_replication_keys = []
    replication_key        = None
    object_type            = ''

    def __init__(self, client, state):
        self.client = client
        self.state = state

    def sync(self, *args, **kwargs):
        raise NotImplementedError("Sync of child class not implemented")

class CatalogStream(Stream):
    replication_method = 'INCREMENTAL'

class FullTableStream(Stream):
    replication_method = 'FULL_TABLE'

class Departments(FullTableStream):
    tap_stream_id  = 'departments'
    key_properties = ['id']
    object_type    = 'DEPARTMENT'

    def sync(self, company_id=None, *args, **kwargs):
        next_url = "True"
        while next_url:
            starting_after = get_starting_after(next_url)
            response = self.client.fetch_departments(
                    company_id,
                    starting_after)
            data = response.get('data', {})
            departments = data.get('data', [])
            for department in departments:
                yield department
            next_url = data.get('next_url', None)
            
class Employments(FullTableStream):
    tap_stream_id  = 'employments'
    key_properties = ['id']
    object_type    = 'EMPLOYMENT'

    def sync(self, *args, **kwargs):
        next_url = "True"
        while next_url:
            starting_after = get_starting_after(next_url)
            response = self.client.fetch_employments(starting_after)
            data = response.get('data', {})
            employments = data.get('data', [])
            for employment in employments:
                yield employment
            next_url = data.get('next_url', None)

class PayStubs(FullTableStream):
    tap_stream_id  = 'pay_stubs'
    key_properties = ['id']
    object_type    = 'PAY_STUB'

    def sync(self, *args, **kwargs):
        next_url = "True"
        while next_url:
            starting_after = get_starting_after(next_url)
            response = self.client.fetch_pay_stubs(starting_after)
            data = response.get('data', {})
            pay_stubs = data.get('data', [])
            for pay_stub in pay_stubs:
                yield pay_stub
            next_url = data.get('next_url', None)

class Payruns(FullTableStream):
    tap_stream_id  = 'payruns'
    key_properties = ['id']
    object_type    = 'PAYRUN'

    def sync(self, *args, **kwargs):
        next_url = "True"
        while next_url:
            starting_after = get_starting_after(next_url)
            response = self.client.fetch_payruns(starting_after)
            data = response.get('data', {})
            payruns = data.get('data', [])
            for payrun in payruns:
                yield payrun
            next_url = data.get('next_url', None)

class People(FullTableStream):
    tap_stream_id  = 'people'
    key_properties = ['id']
    object_type    = 'PEOPLE'

    def sync(self, company_id=None, *args, **kwargs):
        next_url = "True"
        while next_url:
            starting_after = get_starting_after(next_url)
            response = self.client.fetch_people(
                company_id,
                starting_after)
            data = response.get('data', {})
            people = data.get('data', [])
            for person in people:
                yield person
            next_url = data.get('next_url', None)

class TimeDurations(FullTableStream):
    tap_stream_id  = 'time_durations'
    key_properties = ['id']
    object_type    = 'TIME_DURATION'

    def sync(self, *args, **kwargs):
        next_url = "True"
        while next_url:
            starting_after = get_starting_after(next_url)
            response = self.client.fetch_time_durations(starting_after)
            data = response.get('data', {})
            time_durations = data.get('data', [])
            for time_duration in time_durations:
                yield time_duration
            next_url = data.get('next_url', None)

STREAMS = {
    'departments': Departments,
    'employments': Employments,
    'pay_stubs': PayStubs,
    'payruns': Payruns,
    'people': People,
    'time_durations': TimeDurations
}