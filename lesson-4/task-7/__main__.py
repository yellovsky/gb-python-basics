def factorial_generator(i):
    result = 1

    for i in range(i + 1):
        yield i, result
        result *= i + 1


for i, res in factorial_generator(10):
    print(i, res)
