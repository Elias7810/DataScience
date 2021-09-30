k = 1
list1 = [] 
while True:
    inp = input (f"Введите элемент № {k} (q - выйти)\n")
    if inp == "q":
        break
    list1.append (inp)
    k += 1
print (list1)
for i in range (len(list1) - 1):
    if i % 2 == 0:
        list1 [i],list1 [i + 1] = list1 [i + 1], list1 [i]   
print (list1)    

