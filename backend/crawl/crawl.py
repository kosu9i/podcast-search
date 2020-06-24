import urllib.request

import feedparser

url = "https://shirokane-kougyou.fm/feed.xml"

feeds = feedparser.parse(url)
for i, e in enumerate(feeds['entries']):
    for l in e['links']:
        if l['type'] == 'audio/mp3':
            print('Downloading {:03d} ...'.format(i))
            urllib.request.urlretrieve(l['href'], './{:03d}.mp3'.format(i))

