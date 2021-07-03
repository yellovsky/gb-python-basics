from sys import argv

in_arr = list(map(int, argv[1:]))

result = [i for i in in_arr if in_arr.count(i) == 1]

print('result', result)
