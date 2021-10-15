class Car():
    speed = 0
    ispolice = False

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def go(self, spd):
        print(f"Машина {self.name} поехала со скоростью {spd} км/ч ")
        self.speed = spd

    def stop(self):
        if self.speed > 0:
            print(f"Машина {self.name} успешно остановилась")
        else:
            print(f"Машина {self.name} уже стоит!")

    def turn(self, direction):
        if self.speed > 0:
            if direction in ["направо", "налево"]:
                print(f"Машина {self.name} повернула {direction}, скорость - "
                      f"{self.speed} км/ч.")
            else:
                print("Укажите, куда поворачивать")
        else:
            print("Сначала машину нужно завести!")

    def show_speed(self):
        if self.speed:
            print(f"Скорость машины {self.name} составляет {self.speed} км/ч.")
        else:
            print(f"Машина {self.name} стоит!")


class TownCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.pass_number = 4  # Число пассажиров (по умолчанию - 4 )

    def show_speed(self):
        if 0 < self.speed < 60:
            print(f"Скорость машины {self.name} составляет {self.speed} км/ч.")
        elif self.speed > 60:
            print(f"Скорость машины {self.name} превышает максимально "
                  f"разрешенную! (60 км/ч) Немедленно остановите машину!")
        else:
            print(f"Машина {self.name} стоит!")


class SportCar(Car):

    def __init__(self, name, color, max_speed):
        super().__init__(name, color)
        self.max_speed = max_speed


class WorkCar(Car):

    def __init__(self, name, color, capacity):
        super().__init__(name, color)
        self.capacity = capacity  # Грузоподъемность машины в тоннах

    def show_speed(self):
        if 0 < self.speed < 40:
            print(f"Скорость машины {self.name} составляет {self.speed} км/ч.")
        elif self.speed > 40:
            print(f"Скорость машины {self.name} превышает максимально"
                  f"разрешенную! (40 км/ч) Немедленно остановите машину!")
        else:
            print(f"Машина {self.name} стоит!")


class PoliceCar(Car):
    ispolice = True

    def __init__(self, name, color="синий", oncall=True):
        self.name = name
        self.color = color
        self.oncall = oncall  # Добавлена проверка занятости машины


# Примеры применения классов
car = Car("Лада", "черный")
towncar = TownCar("Хюндай", "черный")
sportcar = SportCar("Феррари", "красный", 300)
workcar = WorkCar("Камаз", "красный", 3)
policecar = PoliceCar("УАЗ", oncall=False)
car.go(25)
car.turn("направо")
car.show_speed()
car.stop()

print(f"Число пассажиров в машине {towncar.name} - {towncar.pass_number}")
towncar.go(80)
towncar.show_speed()
towncar.stop()

print(f"Максимальная скорость машины {sportcar.name} - {sportcar.max_speed} км/ч")
print (sportcar.max_speed)

workcar.go(60)
workcar.show_speed()
workcar.stop()

print(f"Машина {policecar.name} находится на вызове" if policecar.oncall == True
      else f"Машина {policecar.name} отдыхает")