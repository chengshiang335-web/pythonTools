import feedparser

url = "https://news.google.com/rss?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"

feed = feedparser.parse(url)

print("頻道標題:", feed.feed.title)
print("文章數量:", len(feed.entries))

for entry in feed.entries:
    print("標題:", entry.title)
    print("連結:", entry.link)
    print("發布時間:", entry.published)
    print("-"*40) 