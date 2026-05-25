from crewai import Crew

from ..tasks.weekly_task import build_weekly_task

from persistence.repository import get_weekly_news


def run_weekly_pipeline():

    rows = get_weekly_news()

    content = ""

    for row in rows:

        content += f"""
        Categoria: {row[0]}

        Title:
        {row[1]}

        Summary:
        {row[2]}

        Hot News:
        {row[3]}

        Relevancy:
        {row[4]}

        ---------------------
        """

    task = build_weekly_task(content)

    crew = Crew(
        agents=[task.agent],
        tasks=[task],
        verbose=True
    )

    result = crew.kickoff()

    with open("reports/weekly_report.md", "w") as f:
        f.write(result.raw)

    print("Created a weekly report.")