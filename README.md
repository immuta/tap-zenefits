# Zenefits :: Tap

A Singer tap for Zenefits.

## Setup :: Developers

If you are already familiar with `Python Poetry` and `python-dotenv` the next few
sections of this readme do not contain any new information; follow the standard
setup process.

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
- API keys can be accessed by calling the `API_KEYS` environment variable and adding
the `["company name"]` key to the end of the call. This enables `API_KEYS` to scale with any number of companies
  - Example: `json.loads(os.getenv("API_KEYS"))["dandelion chocolate"]`

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

This service is designed to be client agnostic, but does require the correct client `API_KEY` to be loaded
from the `API_KEYS` environment variable. To get a client's `API_KEY` use the their company name:

```python
API_KEY = json.loads(os.getenv("API_KEYS"))["company name"]
```

The client's `company_id` also needs to be set from the dictionary of clients in order to use the `fetch_people()`
and `fetch_departments()` endpoints. Here is an example:

```python
# zenefits.py

companies = {
    'dandelion chocolate': '76795'
}


async def main():
    async with aiohttp.ClientSession() as client:
        people_response = await fetch_people(client, companies['dandelion chocolate'])
        employments_response = await fetch_employments(client)
        departments_response = await fetch_departments(client, companies['dandelion chocolate'])
        time_durations_response = await fetch_time_durations(client)

        return people_response, employments_response, departments_response, time_durations_response
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

### `Python Dotenv` Package :: Environment Variables

- [Python Dotenv Docs](https://pypi.org/project/python-dotenv/)
