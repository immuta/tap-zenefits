import json


class Departments:
    schema = {
        "properties": {
            "company": {
                "object": {
                    "type": ["string", "null"]
                },
                "ref_object": {
                    "type": ["string", "null"]
                },
                "url": {
                    "type": ["string", "null"]
                }
            },
            "id": {
                "type": ["string", "null"],
                "key": True
            },
            "name": {
                "type": ["string", "null"]
            },
            "object": {
                "type": ["string", "null"]
            },
            "people": {
                "object": {
                    "type": ["string", "null"]
                },
                "ref_object": {
                    "type": ["string", "null"]
                },
                "url": {
                    "type": ["string", "null"]
                }
            }
        },
    }
