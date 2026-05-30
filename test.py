from fetch import get_headlines
from sentiment import score_headlines

articles = get_headlines("artificial intelligence")
scored = score_headlines(articles)

for article in scored:
    print(f"{article['sentiment']} ({article['score']})  |  {article['title']}")