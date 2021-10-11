#Модуль google_trans у меня не заработал, ошибка NoneType. Такая ошибка у многих, возможно,
#баг в модуле. Пиришлось воспользоваться аналогом
from google_trans_new import google_translator

translator = google_translator()
with open("test4.txt", encoding="UTF-8") as test4:
    content = test4.read().splitlines()
content = [line.split() for line in content]
with open("test4rus.txt", "w", encoding="UTF-8") as test4rus:
    for el in content:
        el[0] = translator.translate(el[0], lang_tgt="ru")
        el = " ".join(el)
        test4rus.write(el + '\n')
