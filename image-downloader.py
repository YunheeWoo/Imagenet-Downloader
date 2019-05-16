import urllib.request
import time

now = time.localtime()
print("Start: %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

id_list = []
count = 0

with open('./wnid_list.txt', encoding='utf8') as f:
    for line in f:
        id_list.append(line[:-1])

with open("./fall11_urls.txt", encoding='utf8') as f:
    for line in f:
        info = line.split("\t")
        wnid = info[0][0:9]

        if wnid in id_list:
            try:
                urllib.request.urlretrieve(info[1], 'G:/Imagenet/' + info[0] + '.jpg')
            except:
                pass

        count = count + 1
        if count % 100000 == 0:
            print('current count: ' + count)

now = time.localtime()
print("End: %04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))