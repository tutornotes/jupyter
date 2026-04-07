import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = {
    'message': [
        "Win a free iPhone now", "Hello, how are you?",
        "Congratulations! You won a lottery", "Are we meeting today?",
        "Claim your free prize", "Let's have lunch tomorrow",
        "You have been selected for a gift", "See you at the office"
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

df = pd.DataFrame(data)
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.25, random_state=42)

vec = TfidfVectorizer()
X_train_vec = vec.fit_transform(X_train)
X_test_vec = vec.transform(X_test)

clf = MultinomialNB()
clf.fit(X_train_vec, y_train)
y_pred = clf.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Predictions:", clf.predict(vec.transform(["Win a brand new car", "Are you free tomorrow?"])))
