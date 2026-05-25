import sqlite3

DB_NAME = "news_database.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,
        link TEXT UNIQUE,

        source TEXT,

        published TEXT,
        collected_at TEXT,

        summary TEXT,

        priority TEXT,
        pre_category TEXT,

        category TEXT,
        relevance_score REAL,
        impact_level TEXT,

        hot_news INTEGER DEFAULT 0,

        executive_summary TEXT,

        processed INTEGER DEFAULT 0,
        summarized INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()