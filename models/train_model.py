import os
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Load and clean data
df = pd.read_csv("C:\\Users\\visma\\Downloads\\sample30 (2).csv")  # Adjust the filename if needed
df = df[['reviews_text', 'user_sentiment']].dropna()

# Encode target variable
df['user_sentiment'] = df['user_sentiment'].map({'Positive': 1, 'Negative': 0})

X = df['reviews_text']
y = df['user_sentiment']

# Vectorize text
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and vectorizer
os.makedirs("models", exist_ok=True)

with open("models/sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved in 'models/' folder.")
