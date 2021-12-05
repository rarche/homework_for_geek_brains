def numb_expo(num_1, num_2):
    """
    raises the 1-st number in expo equal of the 2-nd number
    :param num_1:
    :param num_2:
    :return:
    """
    count = -1
    num_1 = 1 / num_1
    while count != num_2:
        num_1 *= num_1
        count -= 1

    return num_1

print(numb_expo(2, -2))