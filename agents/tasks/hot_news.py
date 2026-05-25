from crewai import Task
from agents.agents import hot_news_detector

def build_hot_news_task(news):

    return Task(

        description=f"""
        Analyze if this news is a HOT NEWS.

        Criteria:
        - High repercussion
        - Technological imapact
        - Important tendency

        news:
        {news["title"]}

        Summary:
        {news["summary"]}

        Answer directly and only in JSON.
        """,

        expected_output="""
        {
            "hot_news": true
        }
        """,

        agent=hot_news_detector
    )