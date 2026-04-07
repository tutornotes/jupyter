#!pip install requests beautifulsoup4 scikit-learn --quiet

import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = """Python is a high-level, interpreted programming language known for its simplicity and readability.
It supports multiple programming paradigms including procedural, object-oriented, and functional programming.
Python has a rich ecosystem of libraries and frameworks that make it popular for web development, data analysis,
artificial intelligence, machine learning, and scientific computing. Its syntax emphasizes code readability,
allowing developers to express concepts in fewer lines of code compared to many other languages.
With a large and active community, Python continues to grow as one of the most widely used programming languages in the world."""

def search(q): return [a["href"] for a in BeautifulSoup(requests.post("https://duckduckgo.com/html/", data={"q":q}).text, "html.parser").select("a.result__a", limit=5)]
def get_text(url):
    try:
        s=BeautifulSoup(requests.get(url,timeout=5).text,"html.parser"); [t.decompose() for t in s(["script","style"])]; return s.get_text(" ")
    except: return ""
def score(d1,d2): return cosine_similarity(TfidfVectorizer(stop_words="english").fit_transform([d1,d2]))[0][1]

results=[]
for s in [x.strip() for x in text.split(".") if x.strip()][:5]:
    for url in search(s):
        sc=score(text,get_text(url))
        if sc>0.3: results.append((url,round(sc*100,2)))

if results:
    for u,v in sorted(results,key=lambda x:x[1],reverse=True): print(f"{u} → Similarity: {v}%")
else: print("No significant plagiarism detected.")

