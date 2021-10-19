class Cell():
    counter = 0

    def __init__(self, number):
        self.number = number
        self.counter += 1

    def __str__(self):
        return f"Клетка с чиcлом ячеек {self.number}"

    def __add__(self, other):
        add_cell = Cell(self.number + other.number)
        self.number = 0
        self.counter -= 1
        return add_cell

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            print("Недопустимая операция")

    def __mul_(self, other):
        self.counter -= 1
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        self.counter -= 1
        return Cell(self.number // other.number)

    def make_order(self, row_num):
        for _ in range(self.number // row_num):
            print(row_num * "*")
        print((self.number % row_num) * "*")


cell1 = Cell(20)

cell2 = Cell(15)


cell1.make_order(6)
