inp = input ("Введите строку из нескольких слов, разделенных пробелами \n")
list1  = inp.split ()
for i, elt in enumerate (list1):
    print (i, elt[:10])