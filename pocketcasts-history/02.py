from datetime import datetime
from uuid import UUID

import niquests
from environs import Env
from gaveta.files import ensure_folder
from pydantic import BaseModel, ConfigDict, HttpUrl, RootModel

from constants import (
    DATA_FOLDER,
    EPISODE_ENDPOINT,
    EPISODES_ENDPOINT,
    HISTORY_OUTPUT_PATH,
    LIST_ENDPOINT,
    SUBSCRIBED_OUTPUT_PATH,
)
from models import PlayingStatus
from utils import get_token, write_model_json


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
    playingStatus: PlayingStatus  # noqa: N815

    model_config = ConfigDict(extra="ignore")


class Episodes(BaseModel):
    episodes: list[Episode]

    model_config = ConfigDict(extra="ignore")


class FullEpisode(BaseModel):
    uuid: UUID
    published: datetime
    duration: int
    title: str
    playingStatus: PlayingStatus  # noqa: N815
    podcastUuid: UUID  # noqa: N815
    podcastTitle: str  # noqa: N815

    model_config = ConfigDict(extra="ignore")


class History(RootModel[list[FullEpisode]]):
    root: list[FullEpisode]

    def __iter__(self):
        return iter(self.root)

    def __len__(self) -> int:
        return len(self.root)


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
        ids.extend(
            episode.uuid
            for episode in episodes.episodes
            if episode.playingStatus == PlayingStatus.played
        )

    return ids


def get_history(token: str, episode_ids: list[UUID]) -> History:
    with niquests.Session(multiplexed=True) as s:
        rs = [
            s.post(EPISODE_ENDPOINT, auth=token, json={"uuid": str(episode_id)})
            for episode_id in episode_ids
        ]
        s.gather()

    episodes = []
    for r in rs:
        try:
            data = r.raise_for_status().json()
            episode = FullEpisode(**data)
            episodes.append(episode)
        except niquests.HTTPError:
            print("Episode not found:", r.request.body)

    return History(episodes)


if __name__ == "__main__":
    ensure_folder(DATA_FOLDER)

    env = Env()
    env.read_env()

    token = get_token(env("POCKET_CASTS_EMAIL"), env("POCKET_CASTS_PASSWORD"))

    subscriptions = get_subscriptions(token)
    episode_ids = get_episode_ids(token, subscriptions)
    history = get_history(token, episode_ids)

    print(f"Number of podcasts: {len(subscriptions.podcasts)}")
    print(f"Number of episodes: {len(history)}")

    write_model_json(subscriptions, SUBSCRIBED_OUTPUT_PATH)
    write_model_json(history, HISTORY_OUTPUT_PATH)
