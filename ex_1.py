class Matrix:
    def __init__(self, atribut):
        self.atribut = atribut

    def __add__(self, second):

        list_1 = []
        for i in self.atribut:
            for elemts in i:
                list_1.append(elemts)

        list_2 = []
        a = 0
        for i in second.atribut:
            a = len(i)
            for elemt in i:
                list_2.append(elemt)

        list_res = list(map(sum, zip(list_1, list_2)))
        len_list = len(list_res)

        def func_for_every_a(num):
            numbs = [item for item in list_res[num:num + a]]
            return numbs

        for elemts in range(len_list // a):
            i = elemts * a
            result = func_for_every_a(i)
            print(result)

    def __str__(self):
        n = 0
        result = ''
        while n < len(self.atribut):
            result += f'{self.atribut[n]} \n'
            n += 1
        return result


my_matrix_1 = Matrix([[22, 23, 24], [21, 22, 31], [14, 22, 1]])
my_matrix_2 = Matrix([[20, -3, 31], [10, 1, 21], [12, 40, 24]])
print(my_matrix_1)
print(my_matrix_2)
my_matrix_1 + my_matrix_2
