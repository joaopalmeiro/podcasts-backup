import niquests

from constants import (
    LOGIN_ENDPOINT,
)
from models import Login


def get_token(email: str, password: str) -> str:
    r = niquests.post(
        LOGIN_ENDPOINT,
        data={"email": email, "password": password, "scope": "webplayer"},
    )
    data = r.json()

    return Login(**data).accessToken
