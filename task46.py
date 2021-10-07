from itertools import count
from itertools import cycle


def num_count(num, num_break):
    if type(num) == int and type(num_break) == int:
        for el in count(num):
            if el > num_break:
                break
            else:
                print(el)
    else:
        print("Вводимые значения должны быть целыми числами!")


num_count(3, 10)


def num_repeat(num_list, num_break):
    if type(num_list) == list and type(num_break) == int:
        x = 0
        for el in cycle(num_list):
            if x > num_break:
                break
            print(el)
            x += 1
    else:
        print("Вводимые значения не соответствуют условию!")


list1 = [12, 7, 5]
num_repeat(list1, 10)
