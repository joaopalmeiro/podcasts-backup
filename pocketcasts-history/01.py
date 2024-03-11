from datetime import datetime
from enum import IntEnum
from pathlib import Path
from urllib.parse import urljoin
from uuid import UUID

import niquests
from environs import Env
from gaveta.files import ensure_folder
from gaveta.json import write_json
from pydantic import BaseModel, ConfigDict

BASE_URL = "https://api.pocketcasts.com/"
LOGIN_ENDPOINT = urljoin(BASE_URL, "/user/login_pocket_casts")
HISTORY_ENDPOINT = urljoin(BASE_URL, "/user/history")

DATA_FOLDER = Path("../data")
OUTPUT_PATH = DATA_FOLDER / "pocketcasts-history.json"
RAW_OUTPUT_PATH = Path("history.json")


class PlayingStatus(IntEnum):
    playing = 2
    played = 3


class Episode(BaseModel):
    uuid: UUID
    published: datetime
    duration: int
    title: str
    playingStatus: PlayingStatus
    playedUpTo: int
    podcastUuid: UUID
    podcastTitle: str
    episodeSeason: int
    episodeNumber: int
    author: str


class History(BaseModel):
    total: int
    episodes: list[Episode]

    model_config = ConfigDict(extra="allow")


def get_token(email, password):
    r = niquests.post(
        LOGIN_ENDPOINT,
        data={"email": email, "password": password, "scope": "webplayer"},
    )
    data = r.json()

    return data["accessToken"]


def get_history(token):
    r = niquests.post(HISTORY_ENDPOINT, auth=token)

    return r.json()


if __name__ == "__main__":
    ensure_folder(DATA_FOLDER)

    env = Env()
    env.read_env()

    token = get_token(env("POCKET_CASTS_EMAIL"), env("POCKET_CASTS_PASSWORD"))
    raw_history = get_history(token)
    write_json(raw_history, RAW_OUTPUT_PATH)

    history = History(**raw_history)

    with OUTPUT_PATH.open(mode="w", encoding="utf-8") as f:
        f.write(history.model_dump_json(indent=2))
        f.write("\n")
