import feedparser

newsArray = []
rss = 'http://www.20minutos.es/rss/'
feed = feedparser.parse(rss)

for key in feed["entries"]: 
    newsArray.append(key["title"])
for new in newsArray:
	print new
