class Worker:
    name = None
    surname = None
    position = None
    __income = {
        'wage': None,
        'bonus': None
    }

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self. surname = surname
        self. position = position
        self.__income['wage'] = wage
        self.__income['bonus'] = bonus

    def get_wage(self):
        return self.__income['wage']

    def get_bonus(self):
        return self.__income['bonus']


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self.get_wage() + self.get_bonus()


position = Position('John', 'Doe', 'Manager', 12000, 3000)

print('position.get_full_name()', position.get_full_name())
print('position.get_total_income()', position.get_total_income())
