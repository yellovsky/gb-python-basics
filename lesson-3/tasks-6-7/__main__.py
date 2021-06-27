# FIRST SOLTION (built in)
def int_func(string):
    """ Function to capitalize words in string

    :param string - input string - space separated words
    :return string of capitalized words
    """
    return ' '.join(map(lambda i: i.strip().capitalize(), string.split(' ')))


# SECOND SOLTION (manual capitalize)
def capitalize_word(raw_word):
    """ Helper function to capitalize one word

    :param raw_word - word, maybe with trailing spaces
    :return capitalized word
    """
    word = raw_word.strip()

    if word == '':
        return ''

    first_char_code = ord(word[0])

    if first_char_code >= ord('a') and first_char_code <= ord('z'):
        return f'{chr(first_char_code - 32)}{word[1:]}'
    else:
        return word


def int_func_2(string):
    """ Function to capitalize words in string

    :param string - input string - space separated words
    :return string of capitalized words
    """
    return ' '.join(map(capitalize_word, string.split(' ')))


# THIRD SOLTION (recursion)
def capitalize_char(char):
    """ Helper function to capitalize one char [a-z]

    :param char - single char to capitalize
    :return capitalized char
    """
    code = ord(char)
    if code >= ord('a') and code <= ord('z'):
        return chr(code - 32)
    else:
        return char


def helper_func(first, last):
    """ Helper recursion function

    :param first - processed part of string
    :param last - part of string to be processed
    :return capitalised string
    """
    if last == '':
        return first
    else:
        prev_char = '' if first == '' else first[-1]
        if prev_char == ' ' and last[0] != ' ':
            return helper_func(first + capitalize_char(last[0]), last[1:])
        else:
            return helper_func(first + last[0], last[1:])


def int_func_3(string):
    """ Function to capitalize words in string

    :param string - input string - space separated words
    :return string of capitalized words
    """
    return helper_func('', string)
