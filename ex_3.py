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

print(numb_sum_max(10,4,12))
