# Понимаю задачу так, что программа включает светофор, он зажигается каким-то
# случайным цветом (но в последовательности К - Ж - З), программа должна 
# дождаться требуемого пользователем цвета и сообщить ему об этом 

import random
import time


class TrafficLight():
    __color = {"красный": 7, "желтый": 2, "зеленый": 5}

    def running(self, newcolor):
        if newcolor not in self.__color:
            print("Ошибка! Укажите красный, желтый или зеленый!")
        else:
            color_list = [["красный", "желтый", "зеленый"], ["желтый", "зеленый", "красный"],
                          ["зеленый", "желтый", "красный"]]
            curr_color = random.choice(color_list)
            for elt in curr_color:
                if elt != newcolor:
                    print(f"Сейчас горит {elt} цвет! Он будет гореть "
                          f"{self.__color.get(elt)} секунд!")
                    time.sleep(self.__color.get(elt))
                else:
                    print(f"Светофор переключен в требуемый - {elt} - цвет!"
                          f" Он будет гореть {self.__color.get(elt)} секунд!")
                    break


tlight1 = TrafficLight()
tlight1.running("зеленый")
    