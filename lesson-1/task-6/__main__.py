initial_speed = int(input('What\'s sportmen initial speed? '))
goal_speed = int(input('What\'s the goal? '))

days_counter = 1

while goal_speed > initial_speed:
    days_counter += 1
    initial_speed *= 1.1

print(f'Sportsmen reach required speed in {days_counter} days')
