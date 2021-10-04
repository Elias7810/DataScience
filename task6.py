def int_func(word):
    word = word.title()
    return (word)


inp = input("Введите строку слов, разделенных пробелами \n")
inp = inp.split()
if all(x.islower() == True and x.isalpha() == True for x in inp):
    for elt in inp:
        print(int_func(elt), end=" ")
else:
    print("Ошибка! Каждое слово должно состоять из маленьких латинских букв")
