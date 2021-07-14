class Complex:
    a = 0
    j = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b

        return Complex(a, b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a

        return Complex(a, b)

    def __str__(self):
        if self.b == 0:
            return f'{self.a}'
        elif self.b > 0:
            return f'{self.a} + {self.b}j'
        else:
            return f'{self.a} - {self.b * -1}j'


complex_1 = Complex(2, 3)
complex_2 = Complex(-1, 1)


print(complex_1 + complex_2)
print(complex_1 * complex_2)
