f = open("test.txt","w")
f.close()

from collections import Counter

with open("test.txt", "r") as f:
    data = f.read()
dic = {}

for k,v in sorted(Counter(data.split()).items(), key= lambda x: x[1], reverse = True):
    print(k,v)

for item in data.split('\n'):
    print(item.upper())
