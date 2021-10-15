from statistics import mean
import json

with open("test7.txt", encoding="UTF-8") as test7:
    content = test7.read().splitlines()
content = [el.split() for el in content]
prof = []
for el in content:
    profit = int(el[2]) - int(el[3])
    el.append(profit)
    if profit >= 0:
        prof.append(profit)
av_prof = mean(prof)
dict1, dict2 = {}, {}
for el in content:
    dict1[el[0]] = el[4]
    dict2["average profit"] = av_prof
list1 = [dict1, dict2]
print(list1)
with open("test7res.json", "w") as test7res:
    json.dump(list1, test7res)
