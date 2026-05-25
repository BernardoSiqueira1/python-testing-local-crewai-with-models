from crewai import Task
from agents.agents import weekly_editor


def build_weekly_task(content):

    return Task(

        description=f"""
        Generate a weekly report in Markdown.

        Organize by:
        - Category
        - Hot news
        - Tendencies
        - Technological impacts

        Content:
        {content}
        """,

        expected_output="""
        Complete report in markdown.
        In portuguese.
        """,

        agent=weekly_editor
    )