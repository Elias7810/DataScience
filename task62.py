class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self, mass, thickness):
        asph_mass = (self._length * self._width * mass * thickness) / 1000
        return asph_mass


road1 = Road(20, 5000)
print(road1.asphalt(25, 5))