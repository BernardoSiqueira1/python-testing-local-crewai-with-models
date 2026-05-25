from pydantic import BaseModel
from typing import Optional

class NewsItem(BaseModel):
    
    title: str
    link: str
    source: str
    published: str
    collected_at: str
    summary: Optional[str] = ""
    category: Optional[str] = None
    relevance_score: Optional[float] = None
    impact_level: Optional[str] = None
    hot_news: Optional[bool] = False