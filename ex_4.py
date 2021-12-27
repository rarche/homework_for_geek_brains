class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        self.direction = direction
        return f'Машина повернула {self.direction}'

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        result = int(super().show_speed())
        if result > 60:
            return 'Превышение скорости'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        result = int(super().show_speed())
        if result > 40:
            return 'Превышение скорости'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name, is_police)
        

my_town_car = TownCar(80,'red','toyota')
my_work_car = WorkCar(50, 'blue', 'mazda')
my_police_car = PoliceCar(100, 'white', 'ford')
print(my_police_car.is_police)
print(my_town_car.show_speed())
print(my_work_car.show_speed())
print(my_police_car.show_speed())
print(my_town_car.turn('направо'))
print(my_work_car.go())
print(my_police_car.stop())


