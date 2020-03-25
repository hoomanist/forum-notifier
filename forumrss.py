import feedparser
import os
url = "https://forum.ubuntu.ir/index.php?action=.xml;type=rss"
feed = feedparser.parse(url)

items = feed["items"]
titles = []
dates = []
for i in items:
    titles.append(i["title"])
    dates.append(i["link"])
last_title = titles[0]
last_date = dates[0]
if os.path.exists("/home/hooman/forum.last"):
    with open("forum.last","r") as file:
        ll = file.read()
        if not ll == str(last_date) + str(last_title):
            os.system("notify-send 'new massage'")
with open("/home/hooman/forum.last","w") as file:
    out = str(last_date) + str(last_title)
    file.write(out)

