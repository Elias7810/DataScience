import sys

list1 = []


def sum_num():
    inp = input("Введите строку чисел, разделенных пробелами (q - выйти) \n")
    inp = inp.split()
    for elt in inp:
        if elt == "q":
            print(sum(list1))
            sys.exit()
        try:
            elt = float(elt)
            list1.append(elt)
        except ValueError:
            print("Ошибка! Вводимыe значения должны быть числами!")
            sys.exit()
    print(sum(list1))
    sum_num()


sum_num()
