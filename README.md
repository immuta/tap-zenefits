# Zenefits :: Tap

A Singer tap for Zenefits.

## Setup :: Developers

- Install Python Poetry: [Poetry](https://python-poetry.org/)
  - Poetry handles dependencies and virtual environments
- After pulling the repo run `poetry install`
  - Ensures all dependencies are the correct version
  - `python-dotenv` is included to handle environment variables
    - A `.env` file will be created if one doesn't exist
      - **Never** add `.env` to version control
    - Add private environment variables to the `.env` file if necessary
    - The `.gitignore` file includes `.env` by default
