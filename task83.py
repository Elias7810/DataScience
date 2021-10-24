class ListValidator(Exception):
    pass


list1 = []
while True:
    flag = True
    n = input("Введите число (q - выйти)\n")
    if n != "q":
        try:
            n = float(n)
        except ValueError:
            flag = False
            raise ListValidator("Должно быть введено число, не строка")
        else:
            list1.append(n)
        finally:
            if flag == False:
                print("Должно быть введено число, не строка")
                continue
            else:
                continue
    else:
        break
print(list1)
