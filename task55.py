with open("test5.txt", "w") as test5:
    test5.write("5 7 12 18 25")
with open("test5.txt", "r") as test5:
    content = test5.read().split()
    content = [float(el) for el in content]
print(sum(content))
