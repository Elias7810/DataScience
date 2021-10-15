class Stationery():
    title = "Канцелярские принадлежности"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("Ручка пишет")


class Penсil(Stationery):

    def draw(self):
        print("Карандаш пишет")


class Handle(Stationery):

    def draw(self):
        print("Маркер пишет")


pen1 = Pen()
pen1.draw()

pencil1 = Penсil()
pencil1.draw()

handle1 = Handle()
handle1.draw()

stat1 = Stationery()
stat1.draw()


# Для закрепления материала проверил, что Python сначала ищет метод в своем классе,
# а потом в родительских в порядке их перечисления в скобках
class Handle2(Handle, Stationery):
    pass


handle2 = Handle2()
handle2.draw()

