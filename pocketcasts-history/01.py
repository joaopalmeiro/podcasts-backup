from datetime import datetime
from uuid import UUID

import niquests
from environs import Env
from gaveta.files import ensure_folder
from pydantic import BaseModel, ConfigDict

from constants import (
    DATA_FOLDER,
    HISTORY_ENDPOINT,
    HISTORY_OUTPUT_PATH,
)
from models import PlayingStatus
from utils import get_token, write_model_json


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

    write_model_json(history, HISTORY_OUTPUT_PATH)
