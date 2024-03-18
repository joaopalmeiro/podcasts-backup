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
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#session-gather:
    - `s.gather()  # resolve all pending "lazy" responses`
  - https://niquests.readthedocs.io/en/latest/api.html#requests.Session
  - https://toolbelt.readthedocs.io/en/latest/sessions.html#baseurlsession
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#make-a-request
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#json-response-content
    - "Since Niquests 3.2, `r.raise_for_status()` is chainable as it returns self if everything went fine."
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#errors-and-exceptions:
    - "`Response.raise_for_status()` will raise an `HTTPError` (...)"
  - https://niquests.readthedocs.io/en/latest/api.html#requests.Response.raise_for_status
  - https://niquests.readthedocs.io/en/latest/api.html#niquests.PreparedRequest
  - https://niquests.readthedocs.io/en/latest/user/authentication.html#passing-a-bearer-token
  - https://niquests.readthedocs.io/en/latest/user/quickstart.html#speedups
  - https://niquests.readthedocs.io/en/latest/api.html#niquests.HTTPError
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
  - https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump
  - https://github.com/pydantic/speedate
  - https://github.com/pydantic/pydantic/issues/6512
- mypy:
  - https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-19
  - https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-local-partial-types
- Ruff:
  - https://github.com/astral-sh/ruff/issues/4014
  - https://docs.astral.sh/ruff/linter/#error-suppression
  - `N815`: https://docs.astral.sh/ruff/rules/mixed-case-variable-in-class-scope/
  - https://docs.astral.sh/ruff/rules/try-except-in-loop/
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/servers/src/main/java/au/com/shiftyjelly/pocketcasts/servers/sync/SyncServer.kt
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/model/src/main/java/au/com/shiftyjelly/pocketcasts/models/to/HistorySyncRequest.kt
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/repositories/src/main/java/au/com/shiftyjelly/pocketcasts/repositories/sync/SyncHistoryTask.kt#L83
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/preferences/src/main/java/au/com/shiftyjelly/pocketcasts/preferences/Settings.kt#L72
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/model/src/main/java/au/com/shiftyjelly/pocketcasts/models/type/EpisodePlayingStatus.kt
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/model/src/main/java/au/com/shiftyjelly/pocketcasts/models/converter/EpisodePlayingStatusConverter.kt
- https://github.com/Automattic/pocket-casts-android/blob/7.58/wear/src/main/kotlin/au/com/shiftyjelly/pocketcasts/wear/ui/episode/EpisodeViewModel.kt#L421: `onArchiveClicked()`
- https://github.com/Automattic/pocket-casts-android/blob/7.58/wear/src/main/kotlin/au/com/shiftyjelly/pocketcasts/wear/ui/episode/EpisodeViewModel.kt#L459: `onMarkAsPlayedClicked()`
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/repositories/src/main/java/au/com/shiftyjelly/pocketcasts/repositories/podcast/EpisodeManagerImpl.kt#L429
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/model/src/main/java/au/com/shiftyjelly/pocketcasts/models/entity/PodcastEpisode.kt#L38: `@ColumnInfo(name = "playing_status") override var playingStatus: EpisodePlayingStatus = EpisodePlayingStatus.NOT_PLAYED`
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/model/src/main/java/au/com/shiftyjelly/pocketcasts/models/entity/PodcastEpisode.kt#L164: `setPlayingStatusInt(status: Int)`
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/features/podcasts/src/main/java/au/com/shiftyjelly/pocketcasts/podcasts/view/podcast/UserEpisodeViewHolder.kt#L194: `val episodeGreyedOut = episode.playingStatus == EpisodePlayingStatus.COMPLETED || episode.isArchived`
- https://github.com/Automattic/pocket-casts-android/blob/7.58/modules/services/repositories/src/main/java/au/com/shiftyjelly/pocketcasts/repositories/podcast/PodcastManagerImpl.kt#L275

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

```python
from pathlib import Path
from gaveta.json import write_json
write_json(subscriptions.model_dump(mode="json"), Path("subscriptions.json"))
```

```python
from pathlib import Path
from gaveta.json import write_json
write_json(episodes, Path("episodes.json"))
```
