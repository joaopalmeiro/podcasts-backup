from uuid import UUID

import niquests
from environs import Env
from gaveta.files import ensure_folder
from pydantic import BaseModel, ConfigDict, HttpUrl

from constants import (
    DATA_FOLDER,
    EPISODES_ENDPOINT,
    LIST_ENDPOINT,
    SUBSCRIBED_OUTPUT_PATH,
)
from utils import get_token


class Subscription(BaseModel):
    uuid: UUID
    title: str
    author: str
    url: HttpUrl

    model_config = ConfigDict(extra="ignore")


class Subscriptions(BaseModel):
    podcasts: list[Subscription]

    model_config = ConfigDict(extra="ignore")


class Episode(BaseModel):
    uuid: UUID

    model_config = ConfigDict(extra="ignore")


class Episodes(BaseModel):
    episodes: list[Episode]

    model_config = ConfigDict(extra="ignore")


def get_subscriptions(token: str) -> Subscriptions:
    r = niquests.post(LIST_ENDPOINT, auth=token)
    data = r.json()

    return Subscriptions(**data)


def get_episode_ids(token: str, subscriptions: Subscriptions) -> list[UUID]:
    with niquests.Session(multiplexed=True) as s:
        rs = [
            s.post(
                EPISODES_ENDPOINT,
                auth=token,
                json=podcast.model_dump(mode="json", include={"uuid"}),
            )
            for podcast in subscriptions.podcasts
        ]
        s.gather()

    ids: list[UUID] = []
    for r in rs:
        data = r.json()
        episodes = Episodes(**data)
        ids.extend(episode.uuid for episode in episodes.episodes)

    return ids


if __name__ == "__main__":
    ensure_folder(DATA_FOLDER)

    env = Env()
    env.read_env()

    token = get_token(env("POCKET_CASTS_EMAIL"), env("POCKET_CASTS_PASSWORD"))

    subscriptions = get_subscriptions(token)
    episode_ids = get_episode_ids(token, subscriptions)

    with SUBSCRIBED_OUTPUT_PATH.open(mode="w", encoding="utf-8") as f:
        f.write(subscriptions.model_dump_json(indent=2))
        f.write("\n")
