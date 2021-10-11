from statistics import mean

with open("test3.txt", encoding="UTF-8") as test3:
    content = test3.read().splitlines()
content = [line.split() for line in content]
dict1 = {}
for line in content:
    dict1[line[0]] = float(line[1])
print("Сотрудники, имеющие оклад менее 20 тыс. р.:")
for k, v in dict1.items():
    if v < 20000:
        print(k)
print(f"\nСредняя величина дохода сотрудников составила {mean(dict1.values())} р.")
