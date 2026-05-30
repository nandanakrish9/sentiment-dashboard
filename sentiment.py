from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def score_headlines(articles):
    results = []
    for article in articles:
        title = article["title"]
        scores = analyzer.polarity_scores(title)
        
        # compound is a single score from -1 (most negative) to +1 (most positive)
        compound = scores["compound"]
        
        if compound >= 0.05:
            sentiment = "Positive"
        elif compound <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        
        results.append({
            "title": title,
            "source": article["source"],
            "published": article["published"],
            "url": article["url"],
            "score": compound,
            "sentiment": sentiment
        })
    
    return results