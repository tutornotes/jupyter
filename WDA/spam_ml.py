# =============================
# Spam Classifier using TF-IDF + Naive Bayes
# =============================

# Required:
# pip install scikit-learn nltk

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nltk.download('stopwords')

# -----------------------------
# a. Dataset
# -----------------------------
data = {
    "message": [
        "Win a free iPhone now",
        "Hello how are you",
        "Congratulations you won a lottery",
        "Are we meeting today",
        "Claim your free prize now",
        "Let's go for lunch",
        "You have been selected for a reward",
        "See you tomorrow"
    ],
    "label": ["spam", "ham", "spam", "ham", "spam", "ham", "spam", "ham"]
}

df = pd.DataFrame(data)

# -----------------------------
# b. Preprocessing
# -----------------------------
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()                         # lowercase
    text = re.sub(r'[^a-z\s]', '', text)        # remove special chars
    tokens = text.split()                       # tokenization
    tokens = [w for w in tokens if w not in stop_words]  # remove stopwords
    return " ".join(tokens)

df["clean_message"] = df["message"].apply(preprocess)

# -----------------------------
# c. Feature Extraction (TF-IDF)
# -----------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["clean_message"])
y = df["label"]

# -----------------------------
# d. Train Model
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

# -----------------------------
# Model Evaluation
# -----------------------------
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# -----------------------------
# e. Test with new messages
# -----------------------------
test_msgs = [
    "Win money now",
    "Are you coming to class",
    "Claim your free reward",
    "Let's meet tomorrow"
]

test_clean = [preprocess(msg) for msg in test_msgs]
test_vec = vectorizer.transform(test_clean)

predictions = model.predict(test_vec)

print("\nPredictions:\n")
for msg, pred in zip(test_msgs, predictions):
    print(f"Message: {msg}")
    print(f"Prediction: {pred}")
    print("-" * 40)