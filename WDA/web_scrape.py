# =============================
# Web Scraping (Public Webpage Simulation)
# =============================

# Required:
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv

# -----------------------------
# STEP a: Send Request
# -----------------------------
url = "https://quotes.toscrape.com/"   # safe public scraping site
response = requests.get(url)

# -----------------------------
# STEP b: Parse HTML
# -----------------------------
soup = BeautifulSoup(response.text, "html.parser")

# -----------------------------
# STEP c: Extract Data
# (Quote = post, Author = user)
# -----------------------------
data = []

quotes = soup.find_all("div", class_="quote")

for q in quotes:
    text = q.find("span", class_="text").get_text(strip=True)
    author = q.find("small", class_="author").get_text(strip=True)

    data.append({
        "author": author,
        "quote": text
    })

# -----------------------------
# STEP d: Store Data (CSV)
# -----------------------------
with open("scraped_data.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["author", "quote"])
    writer.writeheader()
    writer.writerows(data)

# -----------------------------
# STEP e: Display Data
# -----------------------------
print("\nScraped Data:\n")
for item in data:
    print(f"Author: {item['author']}")
    print(f"Quote : {item['quote']}")
    print("-" * 50)