rating  = [7, 5, 3, 3, 2]
inp = int (input ("Введите новый элемент рейтинга \n"))

for elt in rating [::-1]:
    if inp <= elt:
        rating.insert((rating.index (elt) + 1), inp)
        break
if inp > max(rating):
    rating.insert(0, inp)

print (rating)