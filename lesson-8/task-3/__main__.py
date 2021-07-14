class MyNonNumericError(Exception):
    def __init__(self, txt):
        self.txt = txt


arr = []

while True:
    try:
        input_str = input('Enter number, or "stop" to terminate: ')

        if (input_str == 'stop'):
            print(arr)
            break

        if not input_str.isnumeric():
            raise MyNonNumericError('Must be number')

        arr.append(float(input_str))
    except MyNonNumericError:
        print('Must be number')
