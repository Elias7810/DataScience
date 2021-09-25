sales = float (input ("Введите выручку, тыс. р. \n"))
cost = float (input ("Введите издержки, тыс. р. \n"))
profit = sales - cost
if profit > 0:
    print (f"Прибыль составила {profit:.1f} тыс. р.")
    margin = profit/sales
    print (f"Рентабельность составила {margin:.1%}")
    personnel = int (input ("Введите численность фирмы, чел. \n"))
    pers_margin = profit/personnel
    print (f"Прибыль фирмы в расчёте на одного сотрудника составила {pers_margin:.1f} тыс. р.")
elif profit == 0:
    print(f"Выручка фирмы равна ее затратам")
else:
    print (f"Убыток  составил {- profit:.1f} тыс. р.")