# News Sentiment Dashboard

A Streamlit dashboard that fetches recent English headlines for a topic from NewsAPI and classifies each headline as positive, negative, or neutral with VADER sentiment analysis.

## Features

- Search headlines by topic
- Fetch up to 30 articles sorted by publication date
- Classify headline sentiment using VADER's compound score
- Display a sentiment breakdown bar chart
- Show the overall average sentiment score
- List headlines with source, publication date, sentiment, score, and article link

## Requirements

- Python 3.10 or newer
- A [NewsAPI](https://newsapi.org/) API key

Install the Python dependencies:

```powershell
pip install -r requirements.txt
```

## Configuration

`config.py` reads `API_KEY` from Streamlit secrets. Create `.streamlit/secrets.toml` in this project directory:

```toml
API_KEY = "your-newsapi-key"
```

Keep API keys out of source control. The current `fetch.py` also contains a hardcoded NewsAPI key in the request parameters; replace that implementation with the configured secret before sharing or deploying this project.

## Run

From the `sentiment-dashboard` directory:

```powershell
streamlit run app.py
```

Streamlit will print a local URL, normally `http://localhost:8501`.

Enter a topic, then select **Analyze** to fetch and score the latest headlines.

## Sentiment Labels

The VADER compound score ranges from `-1` to `1`:

- **Positive**: score greater than or equal to `0.05`
- **Neutral**: score between `-0.05` and `0.05`
- **Negative**: score less than or equal to `-0.05`

The score is calculated from each headline title, not the full article content.

## Project Structure

```text
sentiment-dashboard/
├── app.py             Streamlit user interface and chart
├── config.py          Streamlit secret configuration
├── fetch.py           NewsAPI headline retrieval
├── sentiment.py       VADER sentiment scoring
├── test.py            Simple command-line scoring check
├── requirements.txt   Python dependencies
└── .streamlit/
    └── secrets.toml   Local API key configuration (not committed)
```

## Data and Limitations

- NewsAPI requires internet access and may enforce rate limits or plan restrictions.
- If NewsAPI returns an error, the dashboard currently displays no results rather than a detailed error message.
- The dashboard analyzes headline text only; it does not read article bodies.
- Results depend on the quality and language of the retrieved headlines.
- This project is for demonstration and analysis purposes.

## Optional Script Check

`test.py` runs a simple fetch-and-score check from the command line:

```powershell
python test.py
```
