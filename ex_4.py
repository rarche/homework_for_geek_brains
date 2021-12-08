def numb_expo(num_1, num_2):
    """
    raises the 1-st number in expo equal of the 2-nd number
    :param num_1:
    :param num_2:
    :return:
    """
    count = -1
    while count != num_2:
        num_1 += num_1
        count -= 1

    return 1 / num_1
a = int(input('Input positive number: '))
b = int(input('Input negative number: '))
print(numb_expo(a, b))