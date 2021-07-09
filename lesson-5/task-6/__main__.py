from os import path


def read_file(filename):
    file_path = path.join(path.dirname(__file__), filename)
    f_obj = open(file_path, "r")

    fie_content = f_obj.readlines()
    f_obj.close()
    return fie_content


def get_str_digits(string):
    result = ''.join(char for char in string if char.isdigit())
    return int(result) if result != '' else 0


def handle_schedule_line(line):
    name, rest = line.split(':')
    raw_vals = [get_str_digits(val)
                for val in rest.split(' ') if val.strip() != '']
    return name, sum(raw_vals)


lines = read_file('schedule.txt')
result = dict([handle_schedule_line(line) for line in lines])

print(result)
