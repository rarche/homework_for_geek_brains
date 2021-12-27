class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def formule(self, mass, amount_of_cm):
        return f'{int(self._lenght) * int(self._width) * int(mass) * int(amount_of_cm) / 1000} Tons'

my_mf_road = Road(1223,5)
print(my_mf_road.formule(30,4))
