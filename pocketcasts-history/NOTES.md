# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://support.pocketcasts.com/knowledge-base/desktop-app/
- https://pypi.org/project/environs/
- https://github.com/postmanlabs/httpbin
- https://httpbin.org/
- Niquests:
  - https://pypi.org/project/niquests/
  - https://blog.devgenius.io/10-reasons-you-should-quit-your-http-client-98fd4c94bef3
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#multiplexed-connection
  - https://niquests.readthedocs.io/en/latest/api.html#requests.Session
  - https://toolbelt.readthedocs.io/en/latest/sessions.html#baseurlsession
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#make-a-request
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#json-response-content
  - https://niquests.readthedocs.io/en/latest/user/authentication.html#passing-a-bearer-token
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
- https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-19
- https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-local-partial-types

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