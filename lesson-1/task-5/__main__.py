income = int(input('What\'s your income: '))
spends = int(input('What\'s your spends: '))

if spends > income:
    print('I\'m so sorry... You will be poor')
else:
    print(f'Your profit margin is {income / spends}')
    employee_number = int(input('How many employees in your company? '))
    income_per_employee = income / employee_number
    print(f'On average, each employee brings you {income_per_employee}')
