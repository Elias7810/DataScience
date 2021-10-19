from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def exp(self):
        pass


class Coat(Clothes):


    def __init__(self, v):
        self.v = v

    def exp(self):
        self.expenditure = round((self.v / 6.5 + 0.5), 2)
        return self.expenditure

    @property
    def get_expenditure(self):
        return self.expenditure

    def __add__(self, other):
        sumc = round(self.expenditure + other.expenditure, 2)
        return sumc


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    def exp(self):
        self.expenditure = round((2 * self.h + 0.3), 2)
        return self.expenditure

    @property
    def get_expenditure(self):
        return self.expenditure

    def __add__(self, other):
        sums = round(self.expenditure + other.expenditure, 2)
        return sums


coat1 = Coat(42)
coat2 = Coat(38)
print(coat1.exp())
print(coat2.exp())

suit1 = Suit(1.50)
suit2 = Suit(1.80)
print(suit1.exp())
print(suit2.exp())

print(coat1.expenditure)
print(coat2.expenditure)
print(suit1.expenditure)
print(suit2.expenditure)

print(coat1 + coat2 + (suit1 + suit2))
