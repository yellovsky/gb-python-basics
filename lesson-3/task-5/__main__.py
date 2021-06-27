result = 0
terminator = '#'


def add_str(accum, string):
    """ Helper functionto parse string and add numbers one by one to passed accum

    :param accum - value numbers add to
    :param string - string to be parsed
    :return accum + numbers in passed string (before terminator symbol)
    """
    for symb in string.split(','):
        if symb.strip() == terminator:
            return accum, True
        else:
            accum += int(symb)

    return accum, False


result = 0

while True:
    in_str = input(
        f'Enter coma-separated numbers. When you want to finish, enter "{terminator}" symbol: ')
    (result, finished) = add_str(result, in_str)

    if finished:
        print('Final result: ', result)
        break
    else:
        print('Intermediate result: ', result)
