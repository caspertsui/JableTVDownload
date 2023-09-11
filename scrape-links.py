#!/usr/bin/env python3
import urllib.request
import re

#connect to a URL
website = urllib.request.urlopen("https://jable.tv/tags/black-pantyhose/")

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"(https?://javble.tv/.*?)"', html)

print(links)