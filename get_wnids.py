from urllib.request import urlopen
from bs4 import BeautifulSoup

input_id = "n00007846"

url_front= "http://image-net.org/api/text/wordnet.structure.hyponym?wnid="

id_list = []
id_list.append(input_id)
index = 0

filename = "wnid_list.txt"
txt = open(filename, "w", encoding='utf8')
txt.write(id_list[0] + "\n")
txt.close()

while True:

    url_full = url_front + id_list[index]

    text = urlopen(url_full)
    ids = str(BeautifulSoup(text, "html.parser"))
    ids = ids.replace("-", "")
    ids = ids.replace("\r", "")
    ids = ids[:len(ids)-1].split("\n")
    for id in ids:
        txt = open(filename, "a")
        if id not in id_list:
            id_list.append(id)
            txt.write(id + "\n")
        txt.close()

    index = index + 1
    if index == len(id_list):
        break