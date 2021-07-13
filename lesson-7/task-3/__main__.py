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

    def make_order(self, in_row):
        full = self.num // in_row
        rest = self.num % in_row

        a_row = '*' * in_row
        full_rows = list(map(lambda _: a_row, range(full)))
        full_rows.append('*' * rest)

        print('full_rows', full_rows)
        return '\n'.join(filter(None, full_rows))
