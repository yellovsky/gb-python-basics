goods = [
    (1, {'name': "компьютер", 'price': 20000, 'count': 5, 'units': "шт."}),
    (2, {'name': "принтер", 'price': 6000, 'count': 2, 'units': "шт."}),
    (3, {'name': "сканер", 'price': 2000, 'count': 7, 'units': "шт."})
]

max_num = 3
fields = ["name", 'price', 'count', 'units']

print('Hello there')

while True:
    cmd = input('What you wanna do next? [list/add/analytics/quit]: ')

    if cmd == 'list':
        for item in goods:
            print(item[0], '-', item[1])

    elif cmd == 'add':
        name = input('Enter name: ')
        price = input('Enter price: ')
        count = input('Enter count: ')
        units = input('Enter units: ')

        max_num += 1

        item = {'name': name, 'price': price, 'count': count, 'units': units, }
        goods.append((max_num, item))
        print('New item added: ', item)

    elif cmd == 'analytics':
        name_list = []
        price_list = []
        count_list = []
        units_list = []

        for (_, item) in goods:
            print('item', item)
            name_list.append(item.get('name'))
            price_list.append(item.get('price'))
            count_list.append(item.get('count'))
            units_list.append(item.get('units'))

        analytics = {
            "name": name_list,
            "price": price_list,
            "count": count_list,
            "units": units_list,
        }
        print('Analytics:', analytics)

    elif cmd == 'quit':
        print('Bye!')
        break

    else:
        print('Unknown command')
