class Cell:
    num = 0

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        if (type(self) != type(other)):
            raise TypeError('Both arguments must be ceils')

        return Cell(self.num + other.num)

    def __sub__(self, other):
        if (type(self) != type(other)):
            raise TypeError('Both arguments must be ceils')

        num = self.num - other.num

        if (num < 1):
            raise TypeError('Second cell musb be smaller than first')

        return Cell(num)

    def __mul__(self, other):
        if (type(self) != type(other)):
            raise TypeError('Both arguments must be ceils')

        return Cell(self.num * other.num)

    def __truediv__(self, other):
        if (type(self) != type(other)):
            raise TypeError('Both arguments must be ceils')

        num = self.num // other.num

        if (num < 1):
            raise TypeError('Second cell musb be smaller than first')

        return Cell(num)


cell_a = Cell(4)
cell_b = Cell(3)

cell_a / cell_b
