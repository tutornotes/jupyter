# =============================
# Basic Web Crawler (Keyword Search)
# =============================

# Required:
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# -----------------------------
# a. Accept keyword from user
# -----------------------------
keyword = input("Enter keyword: ").lower()

# -----------------------------
# b. Starting webpage
# -----------------------------
start_url = "https://www.geeksforgeeks.org/"
max_pages = 10   # limit crawling (important)

visited = set()
to_visit = [start_url]

results = []

# -----------------------------
# Crawling
# -----------------------------
while to_visit and len(visited) < max_pages:
    url = to_visit.pop(0)

    if url in visited:
        continue

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        visited.add(url)

        # -----------------------------
        # d. Search keyword in content
        # -----------------------------
        text = soup.get_text(" ").lower()

        if keyword in text:
            # Extract small snippet (context)
            index = text.find(keyword)
            snippet = text[max(0, index-50): index+50]

            results.append((url, snippet))

        # -----------------------------
        # Extract links for crawling
        # -----------------------------
        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])

            if urlparse(next_url).scheme in ["http", "https"]:
                if next_url not in visited and next_url not in to_visit:
                    to_visit.append(next_url)

    except:
        continue

# -----------------------------
# e. Display Results
# -----------------------------
print("\nResults for keyword:", keyword, "\n")

if results:
    for url, snippet in results:
        print("URL:", url)
        print("Snippet:", snippet.strip())
        print("-" * 60)
else:
    print("No matches found.")