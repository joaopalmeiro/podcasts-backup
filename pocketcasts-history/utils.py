from pathlib import Path

import niquests
from pydantic import BaseModel

from constants import LOGIN_ENDPOINT
from models import Login


def get_token(email: str, password: str) -> str:
    r = niquests.post(
        LOGIN_ENDPOINT,
        data={"email": email, "password": password, "scope": "webplayer"},
    )
    data = r.json()

    return Login(**data).accessToken


def write_model_json(model: BaseModel, output_path: Path) -> None:
    with output_path.open(mode="w", encoding="utf-8") as f:
        f.write(model.model_dump_json(indent=2))
        f.write("\n")
