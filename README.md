# Zenefits :: Tap

A Singer tap for Zenefits.

## Setup :: Developers

- Install: [Python Poetry](https://python-poetry.org/)
  - Poetry handles dependencies and virtual environments
- After pulling the repo run `poetry install`
  - Ensures all dependencies are the correct version
  - `python-dotenv` is included to handle environment variables
    - A `.env` file will be created if one doesn't exist
      - **Never** add `.env` to version control
    - Add private environment variables to the `.env` file if necessary
    - The `.gitignore` file includes `.env` by default
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