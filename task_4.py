n = int (input ("Введите любое натуральное число \n"))
m = 0
while n > 0:
    n = n / 10
    x = int(10*(n - int (n)))
    if m == 0 or x > m:
        m = x
print (m)