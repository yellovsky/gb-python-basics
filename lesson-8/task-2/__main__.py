class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    nominator = int(input("Enter nominator: "))
    denominator = int(input("Enter denominator: "))

    if denominator == 0:
        raise MyZeroDivisionError("denominator must be non zero")

    print(f'Result is {nominator / denominator}')

except MyZeroDivisionError as err:
    print("denominator must be non zero caught")
    print(err)
