import pandas as pd

df = pd.read_csv("data/final_with_sentiment.csv")

score_map = {"Positive": 1, "Neutral": 0, "Negative": -1}
df["sentiment_score"] = df["predicted_sentiment"].map(score_map)

print("Average Market Sentiment Score:", df["sentiment_score"].mean())