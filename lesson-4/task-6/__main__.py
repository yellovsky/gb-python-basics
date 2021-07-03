from itertools import count, cycle

cnt = 10
arr = ['el-1', 'el-2', 'el-3', 'el-4', 'el-5']

cnt_iterator = count(10)
arr_cycle = cycle(arr)

for i in range(10):
    print(next(cnt_iterator), next(arr_cycle))
