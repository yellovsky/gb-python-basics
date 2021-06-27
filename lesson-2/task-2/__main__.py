input_list = input('Enter comma separated list: ').split(',')
cycles_qnt = len(input_list) // 2
result = []

i = 0

while i < len(input_list):
    if i % 2:
        print('11', i)
        result.append(input_list[i - 1])
    elif i + 1 < len(input_list):
        print('22', i)
        result.append(input_list[i + 1])
    else:
        result.append(input_list[i])

    i += 1

print(result)
