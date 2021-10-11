import re

with open("test6.txt", encoding="UTF-8") as test6:
    content = test6.read().splitlines()
content = [el.split(":") for el in content]
dict1 = {}
for el in content:
    for elt in el:
        nums = sum(list(map(int, re.findall(r'\d+', elt))))
        dict1[el[0]] = nums
print(dict1)
