from crewai import Task
from agents.agents import summarizer


def build_summary_task(news):

    return Task(

        description=f"""
        Generate a technical and objective summary:

        News:
        {news["title"]}

        Content:
        {news["summary"]}

        The summary must be focused on:
        - being short
        - technical
        - focused on technology
        """,

        expected_output="""
        Objective and direct summary in pure text, portuguese language.
        """,

        agent=summarizer
    )