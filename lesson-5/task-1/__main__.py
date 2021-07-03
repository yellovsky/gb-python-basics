from os import path


def handle_user_input(file):
    string = input('Enter some string. [to terminate enter blank line]: ')

    if (string != ''):
        file.write(f'{string}\n')
        return True
    else:
        return False


file_path = path.join(path.dirname(__file__), 'res.temp.txt')
f_obj = open(file_path, "a")

while handle_user_input(f_obj):
    pass

f_obj.close()
