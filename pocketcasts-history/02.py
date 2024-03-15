from datetime import datetime
from uuid import UUID

import niquests
from environs import Env
from gaveta.files import ensure_folder
from pydantic import BaseModel, ConfigDict, HttpUrl

from constants import DATA_FOLDER, LIST_ENDPOINT, SUBSCRIBED_OUTPUT_PATH
from utils import get_token


class Subscription(BaseModel):
    uuid: UUID
    title: str
    author: str
    url: HttpUrl
    dateAdded: datetime  # noqa: N815

    model_config = ConfigDict(extra="ignore")


class Subscriptions(BaseModel):
    podcasts: list[Subscription]

    model_config = ConfigDict(extra="ignore")


def get_subscriptions(token: str) -> Subscriptions:
    r = niquests.post(LIST_ENDPOINT, auth=token)
    data = r.json()

    return Subscriptions(**data)


if __name__ == "__main__":
    ensure_folder(DATA_FOLDER)

    env = Env()
    env.read_env()

    token = get_token(env("POCKET_CASTS_EMAIL"), env("POCKET_CASTS_PASSWORD"))

    subscriptions = get_subscriptions(token)

    with SUBSCRIBED_OUTPUT_PATH.open(mode="w", encoding="utf-8") as f:
        f.write(subscriptions.model_dump_json(indent=2))
        f.write("\n")
