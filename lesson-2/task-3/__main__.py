month_num = int(input('Enter month number: '))

# list
season_names = ['winter', 'winter', 'spring', 'spring', 'spring',
                'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']

if (month_num > 12 or month_num < 1):
    print('[list] Month  number must be from 1 to 12')
else:
    print(f'[list] Season is {season_names[month_num-1]}')

# dict
season_dict = {1: 'winter',  2: 'winter', 3: 'spring',  4: 'spring',  5: 'spring',
               6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}

season = season_dict.get(month_num)

if (season is None):
    print('[dict] Month  number must be from 1 to 12')
else:
    print(f'[dict] Season is {season_names[month_num-1]}')
