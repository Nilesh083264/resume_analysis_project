import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

data = pd.read_csv("sample_data.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['category']

model = MultinomialNB()
model.fit(X, y)

joblib.dump(model, "resume_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model and vectorizer saved.")