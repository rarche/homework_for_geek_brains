from time import sleep


class TrafficLight:
    colors = ('red', 'yellow', 'green')
    time = (7, 2, 6)

    def __init__(self):
        self.__color = 'color'

    def running(self):
        while True:
            for i in self.colors:
                self.__color = i
                print(self.__color)
                sleep(self.time[self.colors.index(self.__color)])

my_traffic = TrafficLight()
my_traffic.running()
