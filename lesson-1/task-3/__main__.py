print('It converts n to n + nn + nnn')
num = input('Enter n: ')

result = int(num) + int(num + num) + int(num + num + num)
print(f'{num} + {num}{num} + {num}{num}{num} equals: {result}')
