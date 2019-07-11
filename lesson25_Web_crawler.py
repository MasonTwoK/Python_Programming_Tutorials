import requests
from bs4 import BeautifulSoup


def track_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://thenewboston.com/forum/recent_activity.php?page=﻿"+str(page)
        source_code = requests.get(url)
        some_text = source_code.text
        soup = BeautifulSoup(some_text, "html.parser")
        for link in soup.findAll('a', {'class': 'title text-semibold'}):
            href = link.get('href')
            #title= link.string
            #print(href)
            DeepCrawler(href)
        page += 1

def DeepCrawler(item_url):
    source_code = requests.get(item_url)
    some_text = source_code.text
    soup = BeautifulSoup(some_text, "html.parser")
    for item_name in soup.findAll('h1', {'class':'forum-title no-margin-b no-margin-t inline'}):
        print(item_name.string)

track_spider(3)


