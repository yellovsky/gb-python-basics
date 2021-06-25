def my_power(x, y):
    """ Custom pow function realization

    :param x - base degree
    :param y - degree
    :return x in y power
    """
    if y == 0:
        return 1.0

    negative = y < 0

    if (negative):
        y *= -1

    result = float(x)

    while y > 1:
        result *= x
        y -= 1

    return 1 / result if negative else result
