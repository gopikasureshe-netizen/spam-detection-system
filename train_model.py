import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

data = {
    "message": [
        "Win money now",
        "Free lottery ticket",
        "Claim your prize",
        "Meeting at 5 pm",
        "Project submission tomorrow",
        "Let's have lunch",
        "You won cash reward",
        "Call me when free"
    ],

    "label": [
        "spam",
        "spam",
        "spam",
        "ham",
        "ham",
        "ham",
        "spam",
        "ham"
    ]
}

df = pd.DataFrame(data)

X = df["message"]
y = df["label"]

vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vector, y)

pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved!") 