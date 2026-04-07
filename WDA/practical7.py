#!pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

keyword = input("Enter keyword to search: ").lower()
start_url = "https://www.wikipedia.org/"
max_pages = 10

visited = set()
to_visit = [start_url]
matched_pages = []

while to_visit and len(visited) < max_pages:
    url = to_visit.pop(0)
    if url in visited:
        continue

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        visited.add(url)

        text = soup.get_text(" ").lower()
        if keyword in text:
            matched_pages.append(url)

        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            if urlparse(next_url).scheme in ["http", "https"]:
                if next_url not in visited and next_url not in to_visit:
                    to_visit.append(next_url)

    except:
        continue

print("\nPages containing keyword:", keyword)
for page in matched_pages:
    print(page)

