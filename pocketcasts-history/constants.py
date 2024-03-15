from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://api.pocketcasts.com/"
LOGIN_ENDPOINT = urljoin(BASE_URL, "/user/login_pocket_casts")
HISTORY_ENDPOINT = urljoin(BASE_URL, "/user/history")
LIST_ENDPOINT = urljoin(BASE_URL, "/user/podcast/list")

DATA_FOLDER = Path("../data")
HISTORY_OUTPUT_PATH = DATA_FOLDER / "pocketcasts-history.json"
SUBSCRIBED_OUTPUT_PATH = DATA_FOLDER / "pocketcasts-subscribed-podcasts.json"
