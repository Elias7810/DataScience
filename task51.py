list1 = []
while True:
    inp = input("Введите данные для записи (выход - Enter)\n")
    if inp == "":
        break
    list1.append(inp)
with open("test.txt", "w") as test:
    for line in list1:
        test.write(line + '\n')
