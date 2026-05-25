import json

from crewai import Crew
from ..tasks.collector import build_collector_task
from persistence.repository import save_curated_news


def run_collector_pipeline(raw_news):

    for item in raw_news:

        task = build_collector_task(item)

        crew = Crew(
            agents=[task.agent],
            tasks=[task],
            verbose=True
        )

        result = crew.kickoff()

        try:

            data = json.loads(result.raw)

            if not data["accepted"]:
                continue

            item["priority"] = data["priority"]
            item["pre_category"] = data["pre_category"]

            save_curated_news(item)

            print(f"Curated: {item['title']}")

        except Exception as e:
            print(e)