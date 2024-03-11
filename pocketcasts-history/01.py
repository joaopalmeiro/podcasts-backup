from niquests import Session
from environs import Env
from urllib.parse import urljoin

BASE_URL = "https://api.pocketcasts.com/"
LOGIN_ENDPOINT = urljoin(BASE_URL, "/user/login")

if __name__ == "__main__":
    env = Env()
    env.read_env()
    print(LOGIN_ENDPOINT)

    with Session(multiplexed=True) as s:
        pass
