from os import path

translations = ["Один",
                "Два",
                "Три",
                "Четыре"
                ]


def read_file_lines(filename):
    file_path = path.join(path.dirname(__file__), filename)
    f_obj = open(file_path, "r")

    fie_content = f_obj.readlines()
    f_obj.close()
    return fie_content


def write_file_lines(lines, filename):
    file_path = path.join(path.dirname(__file__), filename)
    f_obj = open(file_path, "w")

    fie_content = [f'{line}\n' for line in lines]
    f_obj.writelines(fie_content)
    f_obj.close()


def handle_line(line):
    num = int(line.split(' - ')[1].strip())
    return f'{translations[num - 1]} - {num}'


en_lines = read_file_lines('en.txt')
ru_lines = list(map(handle_line, en_lines))

write_file_lines(ru_lines, 'en.temp.txt')
