import random
import urllib.request

def DownLoadFromWeb(url):
    x = random.randrange(1, 1001)
    z = str(x) + ".jpg"
    urllib.request.urlretrieve(url, z)

while 1:
    url = input()
    DownLoadFromWeb(url)
