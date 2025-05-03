import joblib

def load_model():
    model = joblib.load("resume_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer

def predict_role(text, model, vectorizer):
    x = vectorizer.transform([text])
    return model.predict(x)[0]