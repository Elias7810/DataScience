class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.num = a + b * 1j

    def __add__(self, other):
        sum_c = self.a + other.a + (self.b + other.b) * 1j
        return sum_c

    def __mul__(self, other):
        mul_c = self.a * other.a - self.b * other.b + (self.b * other.a + self.a * other.b) * 1j
        return mul_c


cnum_1 = ComplexNumber(1, 2)
cnum_2 = ComplexNumber(8, 8)
print(cnum_1.num)
print(cnum_2.num)
print(cnum_1 + cnum_2)
print(cnum_1 * cnum_2)
