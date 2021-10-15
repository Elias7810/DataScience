list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list2 = [el for el in list1[1:] if list1[list1.index(el) - 1] < el]
print(list2)
