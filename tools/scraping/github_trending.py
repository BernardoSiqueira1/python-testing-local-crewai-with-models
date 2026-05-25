import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://github.com/trending"

def fetch_github_trending():

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    repos = soup.find_all("article", class_="Box-row")

    items = []

    for repo in repos:
        title_tag = repo.h2.a

        repo_name = (
            title_tag.get("href", "")
            .replace("/", "")
            .strip()
        )

        repo_link = f"https://github.com{title_tag['href']}"

        description_tag = repo.find("p")

        description = (
            description_tag.text.strip()
            if description_tag else ""
        )

        stars_tag = repo.find_all("span")

        items.append({
            "title": repo_name,
            "link": repo_link,
            "published": datetime.utcnow().isoformat(),
            "summary": description,
            "source": "GitHub Trending",
            "collected_at": datetime.utcnow().isoformat()
        })

    return items