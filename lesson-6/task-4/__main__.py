class Car:
    speed = 0
    color = None
    name = None
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} start diving')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f'{self.name}\'s speed is {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, 'Town Car', False)

    def show_speed(self):
        super().show_speed()

        if (self.speed > 60):
            print(f'{self.name}\'s speed limit exceeded [60]')


class SportCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, 'Sport Car', False)


class WorkCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, 'Work Car', False)

    def show_speed(self):
        super().show_speed()

        if (self.speed > 40):
            print(f'{self.name}\'s speed limit exceeded [40]')


class PoliceCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, 'Police Car', False)


town_car = TownCar(30, 'red')
sport_car = SportCar(120, 'red')
work_car = WorkCar(50, 'red')
police_car = PoliceCar(80, 'red')


town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()
