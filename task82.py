class MyZeroError(Exception):
    pass

def divide ():
    flag = True
    a = input("Введите делимое\n")
    b = input("Введите делитель\n")
    try:
        a = float(a)
        b = float(b)
        if b == 0.0:
            raise MyZeroError  ("Нельзя делить на ноль!")
        else:
            c = a / b
            print (c)
            flag = False
    except ValueError:
        print("Вводимые данные должны быть числами!")
    finally:
        if flag == False:
            print("Работа программы завершена")
        else:
            divide ()

divide ()