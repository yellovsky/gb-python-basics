from sys import argv

in_arr = list(map(int, argv[1:]))

out_arr = [el for index, el in enumerate(
    in_arr[1:]) if el > in_arr[index]]

print(f'First solution: ', out_arr)
