from .rss.rss_reader import read_rss_feed
from .scraping.github_trending import fetch_github_trending
from .api_call.hacker_news import fetch_hackernews
from .rss.feeds import RSS_FEEDS

def collect_all_sources():

    all_news = []

    # RSS
    for feed in RSS_FEEDS:
        try:
            all_news.extend(read_rss_feed(feed))
        except Exception as e:
            print(e)

    # HackerNews
    try:
        all_news.extend(fetch_hackernews())
    except Exception as e:
        print(e)

    # GitHub Trending
    try:
        all_news.extend(fetch_github_trending())
    except Exception as e:
        print(e)

    return all_news