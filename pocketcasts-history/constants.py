from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://api.pocketcasts.com/"
LOGIN_ENDPOINT = urljoin(BASE_URL, "/user/login_pocket_casts")
HISTORY_ENDPOINT = urljoin(BASE_URL, "/user/history")
LIST_ENDPOINT = urljoin(BASE_URL, "/user/podcast/list")
EPISODES_ENDPOINT = urljoin(BASE_URL, "/user/podcast/episodes/bookmarks")
EPISODE_ENDPOINT = urljoin(BASE_URL, "/user/episode")

DATA_FOLDER = Path("../data")
RECENT_HISTORY_OUTPUT_PATH = DATA_FOLDER / "pocketcasts-recent-history.json"
HISTORY_OUTPUT_PATH = DATA_FOLDER / "pocketcasts-history.json"
SUBSCRIBED_OUTPUT_PATH = DATA_FOLDER / "pocketcasts-subscribed-podcasts.json"
