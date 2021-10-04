# Первый способ
def my_func(x, y):
    if x > 0 and type(y) == int and y < 0:
        result = x ** y
        return result
    else:
        print("Неверные исходные данные")


print(my_func(5, -2))


# Второй способ
def my_func(x, y):
    if x > 0 and type(y) == int and y < 0:
        result = 1
        for i in range(abs(y)):
            result = (1 / x) * result
        return result
    else:
        print("Неверные исходные данные")


print(my_func(5, -2))
