#!pip install -q google-api-python-client
import sqlite3
import re
import pandas as pd
from googleapiclient.discovery import build
API_KEY = 'AIzaSyA-HtWIh09SCy6wQB7W7PAqnBrTjvHYTlw'
URLS = [
    "https://www.youtube.com/watch?v=2igLt6EZXH4&t",
    "https://www.youtube.com/watch?v=Y_2y4y0kQig&t",
    "https://www.youtube.com/watch?v=dB6sowSVcZw"
]
conn = sqlite3.connect("youtube_data.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS videos (title TEXT, views INT, likes TEXT)")

youtube = build('youtube', 'v3', developerKey=API_KEY)

print("Scraping data...")
for url in URLS:
    try:

        vid_id = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url).group(1)


        resp = youtube.videos().list(part='snippet,statistics', id=vid_id).execute()

        if resp['items']:
            item = resp['items'][0]
            title = item['snippet']['title']
            views = int(item['statistics'].get('viewCount', 0))
            likes = item['statistics'].get('likeCount', '0')

            c.execute("INSERT INTO videos VALUES (?, ?, ?)", (title, views, likes))
    except Exception as e:
        print(f"Error scraping {url}: {e}")

conn.commit()
print("\n--- DATABASE CONTENTS ---")
df = pd.read_sql_query("SELECT * FROM videos", conn)
display(df)

conn.close()

