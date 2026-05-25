import feedparser
from datetime import datetime

def read_rss_feed(url: str, limit: int = 10):
    feed = feedparser.parse(url)
    items = []

    for entry in feed.entries[:limit]:
        items.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", ""),
            "source": feed.feed.get("title", url),
            "collected_at": datetime.utcnow().isoformat()
        })

    return items