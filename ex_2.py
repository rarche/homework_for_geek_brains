from abc import ABC, abstractmethod


class Cloth(ABC):

    @abstractmethod
    def material(self):
        pass


class Coat(Cloth):
    def __init__(self, h):
        self.h = h

    @property
    def material(self):
        result = self.h / 6.5 + 0.5
        return result


class Costume(Cloth):
    def __init__(self, v):
        self.v = v

    @property
    def material(self):
        result = 2 * self.v + 0.3
        return result

    def sum_material(self, list_s):
        n = 0
        for i in list_s:
            n += i.material
        return n


my_coat = Coat(50)
my_costume_1 = Costume(1.96)
my_costume_2 = Costume(1.24)
my_costume_3 = Costume(1.76)
my_costume_4 = Costume(2.10)
list_costumes = [my_costume_1, my_costume_2, my_costume_3, my_costume_4]
print(my_coat.material)
print(my_costume_1.material)
print(my_costume_1.sum_material(list_costumes))
