from os import path
from random import random


numbers_filename = 'numbers.temp.txt'


def generate_numbers(count):
    return [random() * 100 for _ in range(count)]


def write_file(numbers):
    file_path = path.join(path.dirname(__file__), numbers_filename)
    f_obj = open(file_path, "w")

    fie_content = [f'{num}\n' for num in numbers]
    f_obj.writelines(fie_content)
    f_obj.close()


def read_file():
    file_path = path.join(path.dirname(__file__), numbers_filename)
    f_obj = open(file_path, "r")

    fie_content = f_obj.readlines()
    f_obj.close()
    return fie_content


write_file(generate_numbers(10))

print(f'File sum: {sum([float(num) for num in read_file()])}')
