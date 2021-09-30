assort = int (input ("Введите количество наименований товаров \n"))
i = 0
goods = []
for i in range (assort):
    name = input (f"Введите название товара № {str (i + 1)}\n") 
    price = int (input(f"Введите цену товара № {str (i + 1)}\n"))
    num = int (input(f"Введите количество  товара № {str (i + 1)}\n"))
    unit = input (f"Введите единицу измерения товара № {str (i + 1)}\n") 
    name = {"название": name}
    price = {"цена": price}
    num = {"количество": num}
    unit = {"ед": unit}
    tuple1 = (i + 1, name, price, num, unit)
    goods.append (tuple1)
    i = i + 1
print (goods)  
dict1 = {}
new_goods = list(zip(*goods))
for elt in new_goods [1:]:
    list1 = []
    for el in elt:
        for k, v in el.items ():
            list1.append (v)
            dict1[k] = list1
print (dict1)
