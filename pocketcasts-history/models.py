from typing import Literal

from pydantic import BaseModel, ConfigDict


class Login(BaseModel):
    accessToken: str  # noqa: N815
    tokenType: Literal["Bearer"]  # noqa: N815

    model_config = ConfigDict(extra="ignore")
