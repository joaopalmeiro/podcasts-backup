from datetime import datetime
from enum import IntEnum
from typing import Literal
from uuid import UUID

import niquests
from environs import Env
from gaveta.files import ensure_folder
from pydantic import BaseModel, ConfigDict

from constants import (
    DATA_FOLDER,
    HISTORY_ENDPOINT,
    HISTORY_OUTPUT_PATH,
    LOGIN_ENDPOINT,
)


class PlayingStatus(IntEnum):
    playing = 2
    played = 3


class Episode(BaseModel):
    uuid: UUID
    published: datetime
    duration: int
    title: str
    playingStatus: PlayingStatus  # noqa: N815
    playedUpTo: int  # noqa: N815
    podcastUuid: UUID  # noqa: N815
    podcastTitle: str  # noqa: N815
    episodeSeason: int  # noqa: N815
    episodeNumber: int  # noqa: N815
    author: str

    model_config = ConfigDict(extra="ignore")


class History(BaseModel):
    total: int
    episodes: list[Episode]


class Login(BaseModel):
    accessToken: str  # noqa: N815
    tokenType: Literal["Bearer"]  # noqa: N815

    model_config = ConfigDict(extra="ignore")


def get_token(email: str, password: str) -> str:
    r = niquests.post(
        LOGIN_ENDPOINT,
        data={"email": email, "password": password, "scope": "webplayer"},
    )
    data = r.json()

    return Login(**data).accessToken


def get_history(token: str) -> History:
    r = niquests.post(HISTORY_ENDPOINT, auth=token)
    data = r.json()

    return History(**data)


if __name__ == "__main__":
    ensure_folder(DATA_FOLDER)

    env = Env()
    env.read_env()

    token = get_token(env("POCKET_CASTS_EMAIL"), env("POCKET_CASTS_PASSWORD"))
    history = get_history(token)

    with HISTORY_OUTPUT_PATH.open(mode="w", encoding="utf-8") as f:
        f.write(history.model_dump_json(indent=2))
        f.write("\n")
