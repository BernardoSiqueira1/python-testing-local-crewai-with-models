from crewai import Task
from agents.agents import classifier


def build_classifier_task(news):

    return Task(

        description=f"""
        Analyze the news below.

        Title:
        {news["title"]}

        Summary:
        {news["summary"]}

        Source:
        {news["source"]}

        Classify by:
        - Category
        - Relevance on a scale from 0 to 10
        - Impact:
            low, medium or high

        Answer only in JSON.
        """,

        expected_output="""
        {
            "category": "IA",
            "relevance_score": 8.5,
            "impact_level": "high"
        }
        """,

        agent=classifier
    )