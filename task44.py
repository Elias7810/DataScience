list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Решение через генератор

list2 = [el for el in list1 if list1.count(el) == 1]
print(list2)

# Решение через словарь

dict1 = {}
for el in list1:
    if el not in dict1:
        dict1[el] = 1
    else:
        del dict1[el]
print(list(dict1.keys()))

# С помощью  модуля time проверил, что решение через словарь работает в 4 раза быстрее, чем через count)
