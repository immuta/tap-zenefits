# Zenefits :: Tap

A Singer tap for Zenefits.

## Setup :: Developers

If you are already familiar with `Python Poetry` and `python-dotenv` the next few sections of this `README` do not contain any new information; follow the standard setup process and proceed to the `Usage Notes` section.

### Dependencies and Virtualenvs

- Install: [Python Poetry](https://python-poetry.org/)
  - Poetry handles dependencies and virtual environments
- After pulling the repo run `poetry install`
  - This ensures all dependencies and virtualenvs are the correct version

### Environment Variables

- The `python-dotenv` package is included to handle secret environment variables
- On install a `.env` file will be created in the project root if one doesn't exist
  - **Never** add `.env` to version control!
  - The `.gitignore` file includes `.env` by default
- Add secret environment variables to the `.env` file if necessary
- Each `company_name` environment variable contains stringified `json`
- The Zenefits API key for each company can be accessed by calling the associated `company_name` environment variable with the `token` key. Example:
  - `json.loads(os.getenv("company_name"))["token"]`
- The Zenefits company id for each company can be accessed by calling the `company_name` environment variable with the `company_id` key. Example:
  - `json.loads(os.getenv("company_name"))["company_id"]`
- A new company environment variable should be added to the `.env` file in this format:

```txt
# .env
...

new_company_name='{"token": "Bearer Ks20818dk/2jX", "company_id": "54321"}'
```

### Add native Poetry virtualenv support to VS Code (optional)

- VS Code can be configured to support Poetry virtual environments natively
  - This only needs to be done once
  - Add the following to the VS Code `settings.json` file, or use the `settings` gui:

```json
{
  "python.poetryPath": "poetry",
  "python.venvPath": "~/.cache/pypoetry/virtualenvs"
}
```

- Add a `.vscode` directory to the root of the project
  - Add a `settings.json` file to the `.vscode` directory
  - Ensure `poetry install` has been completed
  - In the terminal run the command `poetry env info` to display the following information:

![Virtualenv Info](https://user-images.githubusercontent.com/10391857/94093631-e4b53480-fdda-11ea-8a97-d9f0dc40be65.png)

- Copy and paste the path from `Virtualenv > Path: </copy/your/path/located/here>` to `settings.json`
within the `.vscode` directory as follows:

```json
{
  "python.pythonPath": "/Users/jww/Library/Caches/pypoetry/virtualenvs/tap-zenefits-kHGAscWf-py3.8"
}
```

- Close and reopen the VS Code terminal
- Poetry virtualenvs are now able to be selected as a default interpreter

New to Poetry? The docs are excellent, and there is more information about
managing environments [here](https://python-poetry.org/docs/managing-environments/).

## Usage Notes

This service is designed to be company agnostic, but it does require the correct company `token` and `company_id` to be loaded from the `company_name` environment variable.

- To access and set a company's `token`:

```python
API_KEY = json.loads(os.getenv("company_name"))["token"]
```

- To access and set a company's `company_id`:

```python
company_id = json.loads(os.getenv("company_name"))["company_id"]
```

- To return data from a single endpoint:

```python
# zenefits.py
...

# Set the company_id and API_KEY for the desired company
company_id = json.loads(os.getenv("company_name"))['company_id']
API_KEY = json.loads(os.getenv("company_name"))['token']

# Set the endpoint function to call; fetch_people() in this example.
async def fetch_endpoint():
    async with aiohttp.ClientSession() as client:
        response = await fetch_people(client, company_id)

        return response

...

loop = asyncio.get_event_loop()
api_response = loop.run_until_complete(fetch_endpoint())
```

- To return data from all endpoints as a list of tuples:

```python
# zenefits.py
...

async def fetch_all_endpoints():
    async with aiohttp.ClientSession() as client:
        people_response = await fetch_people(client, company_id)
        employments_response = await fetch_employments(client)
        departments_response = await fetch_departments(client, company_id)
        time_durations_response = await fetch_time_durations(client)

        return people_response, employments_response, departments_response, time_durations_response

...

loop = asyncio.get_event_loop()
api_response = loop.run_until_complete(fetch_all_endpoints())
```

- The list of tuples will be returned in this order:

```python
api_response == ([people], [employments], [departments], [time_durations])
```

## Zenefits API :: Endpoint Functions

- Payruns Endpoint :: `https://api.zenefits.com/payroll/payruns`
  - [Payruns Docs](https://developers.zenefits.com/v1.0/docs/plt-zpayruns)

```python
async def fetch_payruns(client):
    async with client.get("https://api.zenefits.com/payroll/payruns", headers=headers) as resp:
        response = await resp.json()
        return response
```

- Pay Stubs Endpoint :: `https://api.zenefits.com/payroll/payrun_pay_stubs`
  - [Pay Stubs Docs](https://developers.zenefits.com/docs/payrun-pay-stubs)

```python
async def fetch_pay_stubs(client):
    async with client.get("https://api.zenefits.com/payroll/payrun_pay_stubs", headers=headers) as resp:
        response = await resp.json()
        return response
```

- People Endpoint :: `https://api.zenefits.com/core/companies/{:company_id}/people`
  - [People Docs](https://developers.zenefits.com/docs/people)

```python
async def fetch_people(client, company):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/people", headers=headers) as resp:
        response = await resp.json()
        return response
```

- Employments Endpoint :: `https://api.zenefits.com/core/employments`
  - [Employments Docs](https://developers.zenefits.com/docs/employment)

```python
async def fetch_employments(client):
    async with client.get("https://api.zenefits.com/core/employments", headers=headers) as resp:
        response = await resp.json()
        return response
```

- Departments Endpoint :: `https://api.zenefits.com/core/companies/{:id}/departments`
  - [Departments Docs](https://developers.zenefits.com/docs/department)

```python
async def fetch_departments(client, company):
    async with client.get(f"https://api.zenefits.com/core/companies/{company}/departments", headers=headers) as resp:
        response = await resp.json()
        return response
```

- Time Durations Endpoint :: `https://api.zenefits.com/time_attendance/time_durations`
  - [Time Durations Docs](https://developers.zenefits.com/docs/time-durations)

```python
async def fetch_time_durations(client):
    async with client.get("https://api.zenefits.com/time_attendance/time_durations", headers=headers) as resp:
        response = await resp.json()
        return response
```

## Helpful Documentation

Documentation for packages used in this project.

### `Python Poetry` Package :: Dependency and Environment Management

- [Python Poetry Docs](https://python-poetry.org/docs/)

### `AIOHTTP` Package :: Client and Server Requests

- [AIOHTTP Docs](https://docs.aiohttp.org/en/latest/index.html)

### `VCR.py` Package :: Records API Requests for Testing

- [VCR.py Docs](https://vcrpy.readthedocs.io/en/latest/)

### `Pytest` Package and Plugins :: Testing

- [Pytest Docs](https://docs.pytest.org/en/stable/index.html)
- [Pytest VCR Docs](https://pytest-vcr.readthedocs.io/en/latest/)
- [Pytest Asyncio Docs](https://pypi.org/project/pytest-asyncio/)
- [Pytest Aiohttp Docs](https://pypi.org/project/pytest-aiohttp/)
- [Pytest Cov Docs](https://pytest-cov.readthedocs.io/en/latest/readme.html)

### `Coverage.py` Package :: Test Coverage

- [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.3/)

### `Python Dotenv` Package :: Environment Variables

- [Python Dotenv Docs](https://pypi.org/project/python-dotenv/)

### Zenefits API Documentation

- [Zenefits API Docs](https://developers.zenefits.com/docs/getting-started)
