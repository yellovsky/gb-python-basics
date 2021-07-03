from functools import reduce

numbers = reduce(lambda a, b: a * b, [i for i in range(100, 1001, 2)])

print('numbers', numbers)
