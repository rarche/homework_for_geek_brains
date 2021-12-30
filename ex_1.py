from random import randint

class Matrix:
    def __init__(self, atribut):
        self.atribut = atribut

    def __add__(self, other):
        atribut =[
            [self.atribut[i][j] + other.atribut[i][j] for j in range(len(self.atribut[i]))]
                for i in range(len(self.atribut))]
        return Matrix(atribut)

        # list_1 = []
        # for i in self.atribut:
        #     for elemts in i:
        #         list_1.append(elemts)
        #
        # list_2 = []
        # a = 0
        # for i in second.atribut:
        #     a = len(i)
        #     for elemt in i:
        #         list_2.append(elemt)
        #
        # list_res = list(map(sum, zip(list_1, list_2)))
        # len_list = len(list_res)
        #
        # def func_for_every_a(num):
        #     numbs = [item for item in list_res[num:num + a]]
        #     return numbs
        #
        # for elemts in range(len_list // a):
        #     i = elemts * a
        #     result = func_for_every_a(i)
        #     print(result)

    def __str__(self):
        result = ''
        for i in range(len(self.atribut)):
            for j in range(len(self.atribut[i])):
                result += f'{self.atribut[i][j]:03} '
            result += '\n'
        return result


my_matrix_1 = Matrix([[randint(0,99) for _ in range(10)] for _ in range(10)])
my_matrix_2 = Matrix([[randint(0,98) for _ in range(10)] for _ in range(10)])
print(my_matrix_1)
print(my_matrix_2)
my_matrix_1 + my_matrix_2
