import json

class Employments:
  schema = {
      "properties": {
          "annual_salary": {
              "type": ["string", "null"]
          },
          "comp_type": {
              "type": ["string", "null"]
          },
          "employment_type": {
              "type": ["string", "null"]
          },
          "hire_date": {
              "type": ["string", "null"]
          },
          "id": {
              "type": ["string", "null"],
              "key": True
          },
          "object": {
              "type": ["string", "null"]
          },
          "pay_rate": {
              "type": ["string", "null"]
          },
          "person": {
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
          "termination_date": {
              "type": ["string", "null"]
          },
          "termination_type": {
              "type": ["string", "null"]
          },
          "working_hours_per_week": {
              "type": ["string", "null"]
          },
          "is_active": {
              "type": ["string", "null"]
          }
      }
  }
