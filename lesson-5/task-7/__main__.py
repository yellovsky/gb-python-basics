import json
from os import path

file_path = path.join(path.dirname(__file__), 'firms.txt')
f_obj = open(file_path, "r")


def write_file(obj):
    file_path = path.join(path.dirname(__file__), 'result.temp.txt')
    with open(file_path, 'w') as outfile:
        json.dump(obj, outfile)


def parse_line(line):
    name, _, income, spends = [line.strip()
                               for line in line.split(' ') if line.strip() != '']
    return name, float(income), float(spends)


profit_firms = {}
all_firms = {}

for line in f_obj:
    name, income, spends = parse_line(line)

    profit = income - spends

    all_firms[name] = profit

    if (profit > 0):
        profit_firms[name] = profit

f_obj.close()


result = [all_firms, {"average_profit": sum(
    profit_firms.values())/len(profit_firms)}]

write_file(result)
