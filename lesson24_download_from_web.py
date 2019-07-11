from urllib import request

goog_url = 'http://www.gutenberg.org/files/1160/1160.txt'

def dload_from_web(csv_url):
    r = request.urlopen(csv_url)
    csv = r.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

dload_from_web(goog_url)

