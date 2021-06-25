def my_func(*args):
    """ Helper fuction sum two largest elements of three

    :param first_num - first number 
    :param second_num - second number 
    :param third_num - third number 
    :return sum of two largest numbers
    """
    args_list = list(args)

    if len(args_list) > 3:
        raise ValueError('Function must take 3 numbers')

    args_list.sort(reverse=True)
    return sum(args_list[:2])
