print('Wellcome here!')

name = input('How can I call you? ') or 'Anonymous'


first_string = ''
while not first_string:
    first_string = input(f'{name}, provide some text, please: ')


while first_string == input(f'{name}, provide another text, please: '):
    print('Oh, you\'ve enter the same text')

print('Thakns!')


print('Now, guess some number')
while input('done? [y/n] ') != 'y':
    print('you should guess number')

print('Multiply the number by two')

multiplied_number = int(input('What\'s the result? '))
guessed_number = multiplied_number // 2

print('The guessed number is %d' % guessed_number)

print('Wasn\'t it useless')
