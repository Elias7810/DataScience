a = float (input ("Введите результат первого дня, км. \n"))
b = float (input ("Введите результат второго дня, км. \n"))
i = 1
while i > 0:
    a = a*1.1
    i = i + 1
    if a >= b:
        break
print (i)