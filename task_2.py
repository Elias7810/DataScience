num = int (input ("Введите время в секундах: \n"))
hour = int (num / 3600)
minute  = int ((num - 3600 * hour)/60)
sec = num  - 60 * minute - 3600 * hour
print (f"{hour:02}:{minute:02}:{sec:02}")