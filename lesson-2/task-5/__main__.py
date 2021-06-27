my_list = [7, 5, 3, 3, 2]

print('Initial ratings list:', my_list)


while True:
    rating = int(input('Enter rating: '))
    position = len(my_list)

    while position > 0:
        if my_list[position - 1] >= rating:
            break
        position -= 1

    my_list.insert(position, rating)
    print('Now ratings list is:', my_list)
