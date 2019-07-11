import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,"html.parser")
    for post_text in soup.findAll("a", {"class": "title text-semibold"}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            wordlist.append(each_word)
    clean_up_list(wordlist)

def clean_up_list(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = "?!@#$%^&*()_/.',[]"
        for x in range (0,len(symbols)):
            word = word.replace(symbols[x], "")
        if len(word) > 0:
            clean_list.append(word)
    sorter(clean_list)

def sorter(clean_list):
    sorted_list = {}
    for word in clean_list:
        if word in sorted_list:
            sorted_list[word] += 1
        else:
            sorted_list[word] = 1
    for key, value in sorted(sorted_list.items(), key=operator.itemgetter(1)):
        print(key,value)

start('https://thenewboston.com/forum')

