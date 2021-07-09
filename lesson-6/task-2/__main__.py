class Road:
    _length = 0.0
    _width = 0.0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, weight, height):
        return (self._length * self._width * weight * height)/1000


road = Road(20, 5000)
road.mass(25, 5)
