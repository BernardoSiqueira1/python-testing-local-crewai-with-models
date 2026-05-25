from .news_db import get_connection

def save_news(item):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO news (title, link, source, published, collected_at, summary)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (item["title"], item["link"], item["source"], item["published"], item["collected_at"], item["summary"]))
        conn.commit()
    except Exception as e:
        print(f"Duplicada: {e}")
    finally:
        conn.close()

def get_unprocessed_news(limit=10):
    conn = get_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT id, title, summary, source FROM news WHERE processed = 0 LIMIT ?", (limit,))

    rows = cursor.fetchall()
    conn.close()
    return rows

def save_curated_news(item):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO news (
            title, link, source, published,  collected_at, summary, priority, pre_category ) VALUES (?, ?, ?, ?, ?, ?, ?, ?
            )""",
            (item["title"], item["link"], item["source"], item["published"], item["collected_at"], item["summary"], item["priority"], item["pre_category"])
        )

        conn.commit()

    except Exception as e:
        print(e)

    finally:
        conn.close()

def update_classification(news_id, category, relevance_score, impact_level):
    conn = get_connection()

    cursor = conn.cursor()
    cursor.execute("""
        UPDATE news
        SET category = ?, relevance_score = ?, impact_level = ?, processed = 1
        WHERE id = ?
    """, (category, relevance_score, impact_level, news_id))

    conn.commit()
    conn.close()

def update_hot_news(news_id, hot_news):
    conn = get_connection()

    cursor = conn.cursor()
    cursor.execute("UPDATE news SET hot_news = ? WHERE id = ?", (int(hot_news), news_id))

    conn.commit()
    conn.close()

def get_unsummarized_news(limit=10):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title, summary, source FROM news WHERE summarized = 0 AND processed = 1 LIMIT ?
        """, 
        (limit,)
    )

    rows = cursor.fetchall()
    conn.close()

    return rows

def update_summary(news_id, executive_summary):
    conn = get_connection()

    cursor = conn.cursor()
    cursor.execute("UPDATE news SET executive_summary = ?, summarized = 1 WHERE id = ?", (executive_summary, news_id))

    conn.commit()
    conn.close()

def get_weekly_news():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            category,
            title,
            executive_summary,
            hot_news,
            relevance_score
        FROM news
        WHERE summarized = 1
        ORDER BY relevance_score DESC
        """
    )

    rows = cursor.fetchall()
    conn.close()

    return rows