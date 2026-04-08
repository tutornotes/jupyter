# =============================
# Plagiarism Detection (Final Version - Exam Ready)
# =============================

# Required:
# pip install requests beautifulsoup4 scikit-learn nltk

import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')

# -----------------------------
# a. Input text
# -----------------------------
input_text = input("Enter text to check plagiarism:\n")

# -----------------------------
# b. Preprocessing
# -----------------------------
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [w for w in tokens if w not in stop_words]
    return " ".join(tokens)

# -----------------------------
# c. Web Search (DuckDuckGo)
# -----------------------------
HEADERS = {"User-Agent": "Mozilla/5.0"}

def search_web(query):
    try:
        url = "https://duckduckgo.com/html/"
        response = requests.post(url, headers=HEADERS, data={"q": query})
        soup = BeautifulSoup(response.text, "html.parser")

        links = []
        for a in soup.select("a.result__a", limit=5):
            links.append(a["href"])

        return links
    except:
        return []

def extract_text(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        for tag in soup(["script", "style"]):
            tag.decompose()

        return soup.get_text(" ")
    except:
        return ""

# -----------------------------
# d. Similarity Function
# -----------------------------
def similarity(text1, text2):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(vectors)[0][1]

# -----------------------------
# Reference Dataset (Fallback)
# -----------------------------
reference_docs = [
    "Python is a high level programming language widely used for web development data analysis artificial intelligence and scientific computing",
    "Machine learning is a subset of artificial intelligence that focuses on learning from data",
    "Artificial intelligence is intelligence demonstrated by machines unlike natural human intelligence"
]

# -----------------------------
# e. Sentence-wise Comparison
# -----------------------------
sentences = [s.strip() for s in input_text.split(".") if s.strip()]
results = []

for sentence in sentences[:5]:
    clean_sentence = preprocess(sentence)

    # 1. Compare with web sources
    links = search_web(sentence)

    for link in links:
        print("Checking:", link)   # debug

        page_text = extract_text(link)
        page_sentences = page_text.split(".")[:20]

        for ps in page_sentences:
            ps_clean = preprocess(ps)

            if not ps_clean.strip():
                continue

            score = similarity(clean_sentence, ps_clean)

            if score > 0.2:
                results.append(("WEB: " + link, round(score * 100, 2), ps.strip()))

    # 2. Fallback comparison (guaranteed result)
    for doc in reference_docs:
        score = similarity(clean_sentence, preprocess(doc))

        if score > 0.2:
            results.append(("LOCAL DATASET", round(score * 100, 2), doc))

# -----------------------------
# Output Results
# -----------------------------
print("\nPlagiarism Results:\n")

if results:
    seen = set()
    for source, score, text in sorted(results, key=lambda x: x[1], reverse=True):
        if (source, text) not in seen:
            print(f"Source: {source}")
            print(f"Similarity: {score}%")
            print(f"Matched Text: {text[:100]}")
            print("-" * 60)
            seen.add((source, text))
else:
    print("No significant plagiarism detected.")