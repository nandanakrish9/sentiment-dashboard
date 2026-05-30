import requests
from config import API_KEY

def get_headlines(topic, num_articles=30):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": num_articles,
        "apiKey": "dace758b66514bcfb07d8b876f96afa1"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "ok":
        return []

    articles = []
    for article in data["articles"]:
        articles.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "url": article["url"],
            "published": article["publishedAt"][:10]  # just the date
        })

    return articles
