from abc import ABC, abstractmethod


class Cloth(ABC):

    def __init__(self, title, atr_1):
        self.title = title
        self.atr_1 = atr_1

    @abstractmethod
    def material(self):
        pass


class Coat(Cloth):
    @property
    def material(self):
        result = (int(self.atr_1)/6.5 + 0.5)
        return f'Понадобится {result} метров ткани'


class Costume(Cloth):
    @property
    def material(self):
        result = (int(self.atr_1) * 2 + 0.3)
        return f'Понадобится {result} метров ткани'


my_coat = Coat('favourite coat', 1.5)
my_costume = Costume('favourite_costume', 2.0)
print(my_coat.material)
print(my_costume.material)
