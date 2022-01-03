class Cell:
    def __init__(self, compartments):
        self.compartments = compartments

    def __add__(self, other):
        return f'{int(self.compartments) + int(other.compartments)}'

    def __sub__(self, other):
        if int(self.compartments) >= int(other.compartments):
            return f'{int(self.compartments) - int(other.compartments)}'
        else:
            return 'Невозможно поделить клетки'

    def __mul__(self, other):
        return f'{int(self.compartments) * int(other.compartments)}'

    def __truediv__(self, other):
        return f'{int(self.compartments) // int(other.compartments)}'

    def make_order(self, comp_in_row):

        comp_str = f'*' * self.compartments
        row_count = int(len(comp_str) // int(comp_in_row))
        row_count_back = int(len(comp_str) % int(comp_in_row))
        result = '*' * comp_in_row
        print(f'{result} \n' * row_count, end='')
        print(f'*' * row_count_back)


my_cell_1 = Cell(15)
my_cell_2 = Cell(10)
my_cell_3 = Cell(23)
print(my_cell_1 + my_cell_2)
print(my_cell_1 - my_cell_2)
print(my_cell_1 * my_cell_2)
print(my_cell_1 / my_cell_2)
my_cell_1.make_order(6)
