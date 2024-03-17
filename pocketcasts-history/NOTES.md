# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://support.pocketcasts.com/knowledge-base/desktop-app/
- https://pypi.org/project/environs/
- https://github.com/postmanlabs/httpbin
- https://httpbin.org/
- Niquests:
  - https://pypi.org/project/niquests/
  - https://blog.devgenius.io/10-reasons-you-should-quit-your-http-client-98fd4c94bef3
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#multiplexed-connection:
    - "The only thing you will ever have to do to get started is to specify `multiplexed=True` from within your `Session` constructor."
    - "Any `Response`returned by get, post, put, etc… will be a lazy instance of `Response`."
  - https://niquests.readthedocs.io/en/latest/api.html#requests.Session
  - https://toolbelt.readthedocs.io/en/latest/sessions.html#baseurlsession
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#make-a-request
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#json-response-content
  - https://niquests.readthedocs.io/en/latest/user/authentication.html#passing-a-bearer-token
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#speedups
- Bruno:
  - https://github.com/usebruno/bruno
  - https://docs.usebruno.com/bru-language-tag-reference.html
  - https://github.com/usebruno/bruno-ide-extensions
  - https://marketplace.visualstudio.com/items?itemName=bruno-api-client.bruno
  - https://docs.usebruno.com/secrets-management/dotenv-file.html
  - [.env file not recognized](https://github.com/usebruno/bruno/issues/1757) issue
  - https://docs.usebruno.com/bru-language-samples.html#scripting: `bru.setVar("token", res.body.token);`
  - https://docs.usebruno.com/scripting/sync-requests.html
  - https://docs.usebruno.com/scripting/javascript-reference.html#collection-variables
- Pydantic:
  - https://docs.pydantic.dev/2.6/api/standard_library_types/#uuid
  - https://docs.python.org/3.10/library/uuid.html
  - https://docs.pydantic.dev/2.6/api/standard_library_types/#datetime-types
  - https://docs.pydantic.dev/2.6/api/standard_library_types/#typingliteral
  - https://docs.pydantic.dev/2.6/api/standard_library_types/#enum
  - https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra
  - https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.HttpUrl
- mypy:
  - https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-19
  - https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-local-partial-types
- Ruff:
  - https://github.com/astral-sh/ruff/issues/4014
  - https://docs.astral.sh/ruff/linter/#error-suppression
  - `N815`: https://docs.astral.sh/ruff/rules/mixed-case-variable-in-class-scope/

## Commands

```bash
pip config unset global.require-virtualenv
```

```bash
uv pip sync requirements.txt
```

```bash
uv pip sync --reinstall --refresh --strict requirements.txt
```

## Snippets

```python
with Session(multiplexed=True) as s:
    pass
```

```python
def get_token(email: str, password: str) -> str:
    r = niquests.post(
        LOGIN_ENDPOINT,
        data={"email": email, "password": password, "scope": "webplayer"},
    )
    data = r.json()

    from gaveta.json import write_json
    write_json(data, Path("login.json"))

    return Login(**data).accessToken
```

```python
def get_history(token: str) -> History:
    r = niquests.post(HISTORY_ENDPOINT, auth=token)
    data = r.json()

    from gaveta.json import write_json
    write_json(data, Path("history.json"))

    return History(**data)
```
