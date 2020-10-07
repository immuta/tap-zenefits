import json

class TimeDurations:
  schema = {
      "properties": {
          "person": {
              "url": {
                  "type": ["string", "null"]
              },
              "object": {
                  "type": ["string", "null"]
              },
              "ref_object": {
                  "type": ["string", "null"]
              }
          },
          "activity": {
              "type": ["string", "null"]
          },
          "state": {
              "type": ["string", "null"]
          },
          "valid_status": {
              "type": ["string", "null"]
          },
          "hours": {
              "type": ["string", "null"]
          },
          "date": {
              "type": ["string", "null"]
          },
          "start": {
              "type": ["string", "null"]
          },
          "end": {
              "type": ["string", "null"]
          },
          "is_overnight": {
              "type": ["string", "null"]
          },
          "is_approved": {
              "type": ["string", "null"]
          },
          "approved_datetime": {
              "type": ["string", "null"]
          },
          "approver": {
              "url": {
                  "type": ["string", "null"]
              },
              "object": {
                  "type": ["string", "null"]
              },
              "ref_object": {
                  "type": ["string", "null"]
              }
          },
          "labor_group_ids": {
              "group1": {
                  "type": ["string", "null"]
              }
          },
          "url": {
              "type": ["string", "null"]
          },
          "object": {
              "type": ["string", "null"]
          },
          "id": {
              "type": ["string", "null"],
              "key": True
          }
      },
  }
