#!/usr/bin/env python3

from urllib.request import urlopen, Request
from urllib.parse import quote
import re
import configparser
from bs4 import BeautifulSoup, NavigableString

config = configparser.ConfigParser()
config.read("../config.ini")

url = "https://warthunder.com/en/community/claninfo/"
url += quote(config['OPTIONS']['squadron'])


print(f"opening {url}")
request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

html_bytes = urlopen(request).read()

soup = BeautifulSoup(html_bytes, 'html.parser')

lst = []

for tag in soup.find_all(class_=re.compile("squadrons-members__grid-item")):
    if len(list(soup.children)) > 0:
        for child in tag.children:
            lst.append(str(child.string).strip())

lst = list(filter(None, lst))


for name, score in zip(lst[1::6], lst[2::6]):
    print(f"{name} {score}")
