import json


class People:
    schema = {
        "properties": {
            "banks": {
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
            "city": {
                "type": ["string", "null"]
            },
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
            "country": {
                "type": ["string", "null"]
            },
            "date_of_birth": {
                "type": ["string", "null"]
            },
            "department": {
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
            "employments": {
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
            "first_name": {
                "type": ["string", "null"]
            },
            "preferred_name": {
                "type": ["string", "null"]
            },
            "id": {
                "type": ["string", "null"],
                "key": True
            },
            "employee_number": {
                "type": ["string", "null"]
            },
            "last_name": {
                "type": ["string", "null"]
            },
            "location": {
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
            "manager": {
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
            "object": {
                "type": ["string", "null"]
            },
            "postal_code": {
                "type": ["string", "null"]
            },
            "state": {
                "type": ["string", "null"]
            },
            "status": {
                "type": ["string", "null"]
            },
            "street1": {
                "type": ["string", "null"]
            },
            "street2": {
                "type": ["string", "null"]
            },
            "subordinates": {
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
            "title": {
                "type": ["string", "null"]
            },
            "work_email": {
                "type": ["string", "null"]
            },
            "personal_email": {
                "type": ["string", "null"]
            },
            "work_phone": {
                "type": ["string", "null"]
            },
            "personal_phone": {
                "type": ["string", "null"]
            },
            "gender": {
                "type": ["string", "null"]
            },
            "personal_pronoun": {
                "type": ["string", "null"]
            },
            "photo_url": {
                "type": ["string", "null"]
            },
            "photo_thumbnail_url": {
                "type": ["string", "null"]
            },
            "federal_filing_status": {
                "type": ["string", "null"]
            },
            "social_security_number": {
                "type": ["string", "null"]
            }
        },
    }

