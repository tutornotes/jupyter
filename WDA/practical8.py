#!pip install beautifulsoup4

import os
from bs4 import BeautifulSoup
from collections import defaultdict

folder_path = "local_pages"
os.makedirs(folder_path, exist_ok=True)

html_files = {
    "page1.html": "<html><body><h1>Rose Wood Furniture</h1><p>Rose wood is used for premium furniture.</p></body></html>",
    "page2.html": "<html><body><h1>Flower Shop</h1><p>Fresh rose flowers available here.</p></body></html>",
    "page3.html": "<html><body><h1>Carpentry</h1><p>Quality wood and teak furniture manufacturing.</p></body></html>"
}

for name, content in html_files.items():
    with open(os.path.join(folder_path, name), "w") as f:
        f.write(content)

keywords = input("Enter keywords (comma separated): ").lower().split(",")

results = defaultdict(int)

for file in os.listdir(folder_path):
    if file.endswith(".html"):
        with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        text = soup.get_text(" ").lower()
        score = sum(text.count(k.strip()) for k in keywords)
        if score > 0:
            results[file] = score
print("\nFocused Local Search Results:\n")
for page, score in sorted(results.items(), key=lambda x: x[1], reverse=True):
    print(page, "→ Relevance Score:", score)
