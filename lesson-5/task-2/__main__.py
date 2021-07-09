from os import path


def read_file_lines(filename):
    file_path = path.join(path.dirname(__file__), filename)
    f_obj = open(file_path, "r")

    fie_content = f_obj.readlines()
    f_obj.close()
    return fie_content


def get_words_in_line(line):
    return len([word for word in line.split(' ') if word.strip() != ''])


file_lines = read_file_lines('lorem-ipsum.txt')

print(f'Lines count: {len(file_lines)}')
print('Words in line:')

for i, line in enumerate(file_lines):
    print(f'  line: {i}; words: {get_words_in_line(line)}')
