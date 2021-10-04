def divide(inp1, inp2):
    if inp2 == 0:
        print("Деление на ноль невозможно!")
    else:
        result = inp1 / inp2
        print(result)


a = float(input("Введите делимое \n"))
b = float(input("Введите делитель \n"))
divide(a, b)
