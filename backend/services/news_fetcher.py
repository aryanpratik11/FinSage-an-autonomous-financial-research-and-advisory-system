import requests
from transformers import pipeline

# Initialize summarization pipeline once
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# You can replace this API key later with your own if needed
NEWS_API_KEY = "demo"  # placeholder
NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_latest_news(query: str, limit: int = 5):
    """Fetch latest financial news articles related to a stock or topic."""
    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": limit,
        "sortBy": "publishedAt",
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    if "articles" not in data:
        return []

    news_items = []
    for article in data["articles"]:
        summary = summarize_text(article.get("description") or "")
        news_items.append({
            "title": article.get("title"),
            "url": article.get("url"),
            "source": article.get("source", {}).get("name"),
            "summary": summary
        })
    return news_items


def summarize_news(text: str):
    """Generate a short summary of given text using BART."""
    if not text.strip():
        return "No description available."
    try:
        result = summarizer(text, max_length=60, min_length=20, do_sample=False)
        return result[0]['summary_text']
    except Exception as e:
        print("Summarization error:", e)
        return text[:100] + "..."  
