import singer

LOGGER = singer.get_logger()

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

class CatalogStream(Stream):
    replication_method = 'INCREMENTAL'

class FullTableStream(Stream):
    replication_method = 'FULL_TABLE'

class Departments(FullTableStream):
    tap_stream_id  = 'departments'
    key_properties = ['id']
    object_type    = 'DEPARTMENT'

class Employments(FullTableStream):
    tap_stream_id  = 'employments'
    key_properties = ['id']
    object_type    = 'EMPLOYMENT'

class PayStubs(FullTableStream):
    tap_stream_id  = 'pay_stubs'
    key_properties = ['id']
    object_type    = 'PAY_STUB'

class Payruns(FullTableStream):
    tap_stream_id  = 'payruns'
    key_properties = ['id']
    object_type    = 'PAYRUN'

class People(FullTableStream):
    tap_stream_id  = 'people'
    key_properties = ['id']
    object_type    = 'PEOPLE'

class TimeDurations(FullTableStream):
    tap_stream_id  = 'time_durations'
    key_properties = ['id']
    object_type    = 'TIME_DURATION'