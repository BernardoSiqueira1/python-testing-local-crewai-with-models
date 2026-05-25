from crewai import Task
from agents.agents import collector


def build_collector_task(news):

    return Task(

        description=f"""
        Analyze these collected news.

        Título:
        {news["title"]}

        Resumo:
        {news["summary"]}

        Fonte:
        {news["source"]}

        Determine:

        - If the news are relevant
        - If it's just noise/spam
        - Preliminar category.

        Rules:
        - Ignore spam
        - Ignore clickbait
        - Ignore irrelevant content
        - Prioritize AI, cloud, devOps, security, Open Source and Programming in general.

        Answer only in JSON.
        """,

        expected_output="""
        {
            "accepted": true,
            "priority": "high",
            "pre_category": "IA"
        }
        """,

        agent=collector
    )