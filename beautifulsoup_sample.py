# pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests
import re

# GET
# 支店内CTF問題一覧
r = requests.get('http://10.132.83.231/ctf/question')
soup = BeautifulSoup(r.text, "html.parser") # "html.parser" or "lxml"

# Tag (All)
tags = soup.find_all('a')
print(len(tags))
print(tags[0].text)

# Tag (First One)
tag = soup.find('a')
print(tag.text)

# Tag (First One)
tag = soup.a
print(tag.text)

# Get Tag Attribute
print(tag.get("href"))

# Search Tag
tags = soup.find_all("a", href="/ctf/question/1")
print(len(tags))
print(tags[0].text)

tags = soup.find_all("a", href=re.compile("/1$"))
print(len(tags))
print(tags[0].text)

# CSS Selector
tags = soup.select('a[href$="/1"]')
print(len(tags))
print(tags[0].text)

tags = soup.select('a[href^="/ctf/"]')
print(len(tags))
print(tags[0].text)


# POST
# 支店内CTF第一問目
r = requests.get('http://10.132.83.231/ctf/question/1')
print(r.text)


