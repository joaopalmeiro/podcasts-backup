# pocketcasts-history

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Script to download Pocket Casts podcast history via the Web Player API.

## Development

Install [pyenv](https://github.com/pyenv/pyenv) (if necessary).

Generate the `.env` file and set the environment variables:

```bash
cp .env.example .env && cp .env.example Pocket\ Casts\ Web\ Player\ API/.env
```

```bash
pyenv install && pyenv versions
```

```bash
pip install uv==0.1.24 && uv --version
```

```bash
uv venv .venv
```

```bash
source .venv/bin/activate
```

```bash
which python && python --version
```

```bash
uv pip install -r requirements.txt
```

```bash
uv pip list --strict
```

```bash
uv pip check --verbose
```

```bash
ruff check
```

```bash
mypy
```

```bash
ruff check --fix
```

```bash
ruff format
```

```bash
python 01.py
```

```bash
python 02.py
```

Clear the list of recently listened to episodes ([History](https://play.pocketcasts.com/history)) from Pocket Casts.

```bash
deactivate
```
