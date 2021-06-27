input_str = input('Enter some string: ')

for idx, val in enumerate(input_str.split(' ')):
    print(idx, val if len(val) < 10 else val[:10])
