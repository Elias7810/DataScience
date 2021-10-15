class Worker():

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_full_income(self):
        print(sum(self._income.values()))


pos1 = Position("Ivan", "Ivanov", "engineer", 1000, 25000)

pos1.get_full_name()
pos1.get_full_income()
print (pos1._income)
print (dir (pos1))
