import pickle
import pandas as pd

# Load sentiment model and vectorizer
with open('models/sentiment_model.pkl', 'rb') as f:
    sentiment_model = pickle.load(f)

with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load product review data
df = pd.read_csv("C:\\Users\\visma\\Downloads\\sample30 (2).csv")
df.dropna(subset=["reviews_text", "reviews_username", "name"], inplace=True)

# Map sentiment for consistency
df['user_sentiment'] = df['user_sentiment'].map({'Positive': 1, 'Negative': 0})

# Predict sentiment
df["predicted_sentiment"] = sentiment_model.predict(vectorizer.transform(df["reviews_text"]))

# Define recommendation function
def get_user_recommendations(username):
    user_reviews = df[df['reviews_username'].str.lower() == username.lower()]

    if user_reviews.empty:
        return ["No reviews found for this user."]

    positive_reviews = user_reviews[user_reviews["predicted_sentiment"] == 1]

    if positive_reviews.empty:
        return ["No positive sentiment products to recommend."]

    return positive_reviews["name"].unique().tolist()
