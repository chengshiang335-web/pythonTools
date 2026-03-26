import feedparser

url = "http://rss.cnn.com/rss/edition_world.rss"

feed = feedparser.parse(url)

for entry in feed.entries[:5]:
    print("標題:", entry.get("title", "無標題"))
    print("連結:", entry.get("link", "無連結"))
    print("時間:", entry.get("published", entry.get("updated", "無提供時間")))
    print("-"*50)