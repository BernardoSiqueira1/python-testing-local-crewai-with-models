from crewai import Crew

from ..tasks.summarizer import build_summary_task

from persistence.repository import (
    get_unsummarized_news,
    update_summary
)

def run_summary_pipeline():

    news_list = get_unsummarized_news()

    for row in news_list:

        news = {
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "source": row[3]
        }

        task = build_summary_task(news)

        crew = Crew(
            agents=[task.agent],
            tasks=[task],
            verbose=True
        )

        result = crew.kickoff()

        update_summary(
            news["id"],
            result.raw
        )

        print(f"Summary: {news['title']}")