def numb_sum_max(num_1, num_2, num_3):
    """
    Give sum of two highest numbers in list
    :param num_1: int
    :param num_2: int
    :param num_3: int
    :return: int
    """
    numb_list = [num_1, num_2, num_3]
    numb_min = min(numb_list)
    numb_list.remove(numb_min)
    numb_sum = numb_list[0] + numb_list[1]
    return numb_sum


a = int(input('input 1-st number: '))
b = int(input('input 2-nd number: '))
c = int(input('input 3-rd number: '))
print(numb_sum_max(a, b, c))
