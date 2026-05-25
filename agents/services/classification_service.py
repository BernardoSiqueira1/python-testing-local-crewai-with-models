import json

from crewai import Crew

from ..tasks.classifier import build_classifier_task

from persistence.repository import (
    get_unprocessed_news,
    update_classification
)

def run_classification_pipeline():

    news_list = get_unprocessed_news()

    for row in news_list:

        news = {
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "source": row[3]
        }

        task = build_classifier_task(news)

        crew = Crew(
            agents=[task.agent],
            tasks=[task],
            verbose=True
        )

        result = crew.kickoff()

        try:

            data = json.loads(result.raw)

            update_classification(
                news["id"],
                data["category"],
                data["relevance_score"],
                data["impact_level"]
            )

            print(f"Classified: {news['title']}")

        except Exception as e:
            print(e)