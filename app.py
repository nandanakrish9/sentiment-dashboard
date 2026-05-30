import streamlit as st
import plotly.express as px
import pandas as pd
from fetch import get_headlines
from sentiment import score_headlines

st.title("News Sentiment Dashboard")

topic = st.text_input("Enter a topic to analyze:", "artificial intelligence")

if st.button("Analyze"):
    with st.spinner("Fetching headlines..."):
        articles = get_headlines(topic)
        scored = score_headlines(articles)
        df = pd.DataFrame(scored)

    # ── Summary counts ──
    counts = df["sentiment"].value_counts().reset_index()
    counts.columns = ["Sentiment", "Count"]

    fig = px.bar(
        counts,
        x="Sentiment",
        y="Count",
        color="Sentiment",
        color_discrete_map={
            "Positive": "#2ecc71",
            "Negative": "#e74c3c",
            "Neutral": "#95a5a6"
        },
        title=f'Sentiment Breakdown for "{topic}"'
    )
    st.plotly_chart(fig)

    # ── Average score ──
    avg = df["score"].mean()
    st.metric("Overall Sentiment Score", f"{avg:.3f}", 
              delta="Leaning Positive" if avg > 0 else "Leaning Negative")

    # ── Article table ──
    st.subheader("All Headlines")
    for _, row in df.iterrows():
        color = "#2ecc71" if row["sentiment"] == "Positive" else \
                "#e74c3c" if row["sentiment"] == "Negative" else "#95a5a6"
        st.markdown(
            f'<span style="color:{color}">●</span> **{row["sentiment"]}** ({row["score"]:.2f}) — '
            f'[{row["title"]}]({row["url"]}) *{row["source"]}*',
            unsafe_allow_html=True
        )