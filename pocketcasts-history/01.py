from urllib.parse import urljoin

import niquests
from environs import Env

BASE_URL = "https://api.pocketcasts.com/"
LOGIN_ENDPOINT = urljoin(BASE_URL, "/user/login_pocket_casts")
HISTORY_ENDPOINT = urljoin(BASE_URL, "/user/login_pocket_casts")


def get_token(email, password):
    r = niquests.post(
        LOGIN_ENDPOINT,
        data={"email": email, "password": password, "scope": "webplayer"},
    )
    data = r.json()

    return data["accessToken"]


if __name__ == "__main__":
    env = Env()
    env.read_env()

    token = get_token(env("POCKET_CASTS_EMAIL"), env("POCKET_CASTS_PASSWORD"))
    print(token)
