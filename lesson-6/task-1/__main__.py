import time


class TrafficLight:
    __color = 'green'

    def running(self):
        print(f'Current color: {self.__color}')

        if (self.__color == 'green'):
            time.sleep(5)
            self.__color = 'red'
            self.running()
        elif (self.__color == 'red'):
            time.sleep(7)
            self.__color = 'yellow'
            self.running()
        elif (self.__color == 'red'):
            time.sleep(2)
            self.__color = 'green'
            self.running()


traffic_light = TrafficLight()
traffic_light.running('green')
