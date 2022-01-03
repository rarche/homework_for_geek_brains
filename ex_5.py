class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def com_num(self):
        return f'{int(self.a)} + {int(self.b)}i'

    def __add__(self, other):
        if self.b + other.b > 0:
            return f'{self.a + other.a}+{self.b + other.b}i'
        elif self.b + other.b == 0:
            return f'{self.a + other.a}'
        else:
            return f'{self.a + other.a}{self.b + other.b}i'

    def __mul__(self, other):
        if (self.b * other.a) + (self.a * other.b) == 0:
            return f'{(self.a * other.a) - (self.b * other.b)}'
        elif (self.a * other.a) - (self.b * other.b) == 0:
            return f'{(self.b * other.a) + (self.a * other.b)}i'
        elif (self.b * other.a) + (self.a * other.b) < 0:
            return f'{(self.a * other.a) - (self.b * other.b)}{(self.b * other.a) + (self.a * other.b)}i'
        else:
            return f'{(self.a * other.a) - (self.b * other.b)}+{(self.b * other.a) + (self.a * other.b)}i'


my_complex_1 = ComplexNumber(1, 3)
my_complex_2 = ComplexNumber(4, -5)
my_complex_3 = ComplexNumber(1, -1)
my_complex_4 = ComplexNumber(3, 6)
print(ComplexNumber.__add__(my_complex_1, my_complex_2))
print(ComplexNumber.__mul__(my_complex_3, my_complex_4))
