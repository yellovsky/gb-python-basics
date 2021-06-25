def divide(numerator, denominator):
    """Get result of division of numerator and denominator.

    :param numerator: Numerator.
    :param denominator: Denominator.
    :return: Division result.
    """

    try:
        return numerator / denominator
    except ZeroDivisionError:
        print('Zero division exception detected')


numerator = float(input('Enter numerator: '))
denominator = float(input('Enter denominator: '))

result = divide(numerator, denominator)

if result != None:
    print('result is:', result)
