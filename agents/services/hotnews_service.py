import json

from crewai import Crew

from ..tasks.hot_news import build_hot_news_task

from persistence.repository import (
    get_unprocessed_news,
    update_hot_news
)

def run_hot_news_pipeline():
    news_list = get_unprocessed_news()

    for row in news_list:
        news = {
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "source": row[3]
        }

        task = build_hot_news_task(news)

        crew = Crew(
            agents=[task.agent],
            tasks=[task],
            verbose=True
        )

        result = crew.kickoff()

        try:
            data = json.loads(result.raw)

            update_hot_news(
                news["id"],
                data["hot_news"]
            )

            print(f"Hot News: {news['title']}")

        except Exception as e:
            print(e)