def my_func(x, y, z):
    list1 = [x, y, z]
    list1.sort()
    summax = list1[-1] + list1[-2]
    return summax


print(my_func(19, 12, 5))
