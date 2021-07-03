from sys import argv

work_hours, payment_rate, award = map(int, argv[1:])

salary = (work_hours * payment_rate) + award

print(f'Result salary is {salary}')
