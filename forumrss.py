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
if os.path.exists("$HOME/forum.last"):
    with open("forum.last","r") as file:
        ll = file.read()
        if not ll == str(last_date) + str(last_title):
            os.system("notify-send 'new massage' && cvlc $HOME/audio.mp3")
with open("$HOME/forum.last","w") as file:
    out = str(last_date) + str(last_title)
    file.write(out)

