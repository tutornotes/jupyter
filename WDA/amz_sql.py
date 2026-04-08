import requests
from bs4 import BeautifulSoup
import sqlite3

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
    "Accept-Language": "en-US,en;q=0.9"
}

conn = sqlite3.connect("amazon_products.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    price TEXT,
    rating TEXT
)
""")
conn.commit()

def scrape_amazon(url):
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.find("span", id="productTitle")
    price = soup.find("span", class_="a-price-whole")
    rating = soup.find("span", class_="a-icon-alt")
    return (
        title.get_text(strip=True) if title else "Not Found",
        price.get_text(strip=True) if price else "Not Found",
        rating.get_text(strip=True) if rating else "Not Found"
    )

title, price, rating = scrape_amazon("https://www.amazon.in/d/B0DZF1485D")
cursor.execute(
    "INSERT INTO products (title, price, rating) VALUES (?, ?, ?)",
    (title, price, rating)
)
conn.commit()

print("\nData Inserted\n")
print("{:<5} {:<80} {:<10} {:<20}".format("ID", "TITLE", "PRICE", "RATING"))
print("-"*120)

cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print("{:<5} {:<80} {:<10} {:<20}".format(row[0], row[1][:75], row[2], row[3]))

conn.close()