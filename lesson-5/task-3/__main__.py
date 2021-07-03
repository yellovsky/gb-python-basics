from os import path

salary_limit = 20_000


def read_file_lines(filename):
    file_path = path.join(path.dirname(__file__), filename)
    f_obj = open(file_path, "r")

    fie_content = f_obj.readlines()
    f_obj.close()
    return fie_content


def split_salary_row(row):
    name, salary = row.split(' ')
    return name.strip(), float(salary.strip())


def filter_by_salary(minimal_salary, rows):
    return [row for row in rows if row[1] < minimal_salary]


def get_average_salary(rows):
    return sum([salary for _, salary in rows]) / len(rows)


salaries_rows = read_file_lines('salary.txt')
splitted_rows = list(map(split_salary_row, salaries_rows))
poor_employees = filter_by_salary(20_000, splitted_rows)
poor_employees_names = ', '.join([name for name, _ in poor_employees])

print(f'Employees with salary < {20_000}: {poor_employees_names}')
print(f'Average salary is {get_average_salary(splitted_rows)}')
