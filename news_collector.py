from tools.unified_data_collector import collect_all_sources

from persistence.news_db import init_db
from persistence.repository import save_news

from agents.services.collector_service import run_collector_pipeline
from agents.services.classification_service import run_classification_pipeline
from agents.services.hotnews_service import run_hot_news_pipeline
from agents.services.summary_service import run_summary_pipeline
from agents.services.weeklyreport_service import run_weekly_pipeline


def run_news_collector():

    init_db()

    print("Collecting raw news...")

    raw_news = collect_all_sources()

    print("Collector AI pipeline...")
    run_collector_pipeline(raw_news)

    print("Classification pipeline...")
    run_classification_pipeline()

    print("Hot news pipeline...")
    run_hot_news_pipeline()

    print("Summary pipeline...")
    run_summary_pipeline()

    print("Weekly report...")
    run_weekly_pipeline()

    print("Done.")


run_news_collector()