num = int(input('Enter number: '))

greatest_digit = 0


while num > 0:
    last_digit = num % 10
    num = num // 10
    if (last_digit > greatest_digit):
        greatest_digit = last_digit

print(f'Greatest digit is: {greatest_digit}')
