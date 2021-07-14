def add_rows(row_a, row_b):
    if (len(row_a) != len(row_b)):
        raise TypeError('Row lens mus be equal')

    return [row_a[i] + row_b[i] for i in range(len(row_a))]


class Matrix:
    rows = []

    def __init__(self, rows):
        row_dimensions = [len(row) for row in rows]

        for index, d in enumerate(row_dimensions[1:]):
            if (d != row_dimensions[index]):
                raise TypeError('It\'s not a matrix')

        self.rows = rows

    def __add__(self, other):
        self_dimensions = self.get_dimensions()
        other_dimensions = other.get_dimensions()

        if (self_dimensions != other_dimensions):
            raise TypeError('Matices must have same dimensions')

        rows = [add_rows(self.rows[i], other.rows[i])
                for i in range(self.get_dimensions()[0])]

        return Matrix(rows)

    def __str__(self):
        result = ''

        for row in self.rows:
            str_row = [f'{el:4}' for el in row]
            result += ', '.join(str_row) + '\n'

        return result

    def get_dimensions(self):
        return len(self.rows), len(self.rows[0])
