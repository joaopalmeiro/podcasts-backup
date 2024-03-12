from datetime import datetime
from enum import IntEnum
from pathlib import Path
from urllib.parse import urljoin
from uuid import UUID

import niquests
from environs import Env
from gaveta.files import ensure_folder
from pydantic import BaseModel, ConfigDict

BASE_URL = "https://api.pocketcasts.com/"
LOGIN_ENDPOINT = urljoin(BASE_URL, "/user/login_pocket_casts")
HISTORY_ENDPOINT = urljoin(BASE_URL, "/user/history")

DATA_FOLDER = Path("../data")
OUTPUT_PATH = DATA_FOLDER / "pocketcasts-history.json"


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


def get_token(email: str, password: str) -> str:
    r = niquests.post(
        LOGIN_ENDPOINT,
        data={"email": email, "password": password, "scope": "webplayer"},
    )
    data = r.json()

    return data["accessToken"]


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

    with OUTPUT_PATH.open(mode="w", encoding="utf-8") as f:
        f.write(history.model_dump_json(indent=2))
        f.write("\n")
