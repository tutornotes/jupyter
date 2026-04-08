# =============================
# Text Mining + Webpage Preprocessing
# =============================

# Required:
# pip install requests beautifulsoup4 nltk

import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# -----------------------------
# a. Fetch Webpage
# -----------------------------
url = "https://www.geeksforgeeks.org/"
response = requests.get(url)

# -----------------------------
# b. Parse HTML
# -----------------------------
soup = BeautifulSoup(response.text, "html.parser")

# -----------------------------
# c. Extract Meta Information
# -----------------------------
title = soup.title.string if soup.title else "Not Available"

meta_description = "Not Available"
meta_keywords = "Not Available"

for tag in soup.find_all("meta"):
    if tag.get("name") == "description":
        meta_description = tag.get("content")
    if tag.get("name") == "keywords":
        meta_keywords = tag.get("content")

# -----------------------------
# Extract visible text (remove scripts/styles)
# -----------------------------
for element in soup(["script", "style"]):
    element.decompose()

text = soup.get_text(separator=" ")

# -----------------------------
# d. Text Preprocessing
# -----------------------------
# lowercase
text = text.lower()

# remove special characters
text = re.sub(r"[^a-z\s]", "", text)

# remove stopwords
stop_words = set(stopwords.words("english"))
tokens = text.split()
filtered_words = [w for w in tokens if w not in stop_words]

processed_text = " ".join(filtered_words)

# -----------------------------
# e. Display Output
# -----------------------------
print("\n===== META INFORMATION =====\n")
print("Title:", title)
print("Description:", meta_description)
print("Keywords:", meta_keywords)

print("\n===== PROCESSED TEXT (Sample) =====\n")
print(processed_text[:500])  # show first 500 characters