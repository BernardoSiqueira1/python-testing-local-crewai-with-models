import requests
from datetime import datetime

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def fetch_hackernews(limit=20):

    story_ids = requests.get(
        f"{BASE_URL}/topstories.json"
    ).json()

    items = []

    for story_id in story_ids[:limit]:

        data = requests.get(
            f"{BASE_URL}/item/{story_id}.json"
        ).json()

        if not data:
            continue

        items.append({
            "title": data.get("title", ""),
            "link": data.get("url", ""),
            "published": datetime.utcfromtimestamp(data.get("time", 0)).isoformat(),
            "summary": "",
            "source": "Hacker News",
            "collected_at": datetime.utcnow().isoformat(),
            "score": data.get("score", 0),
            "comments": data.get("descendants", 0)
        })

    return items