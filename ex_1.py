def divide_numb (num_1, num_2):
    """
    Divides first number on second number
    :param num_1:int
    :param num_2:int
    :return:int
    """
    if num_2 == 0:
        result = 'Phew! Universe is safe. But please, be careful next time.'
    else:
        result = num_1 // num_2
    return result

num_1 = int(input('Please, input 1-st number: '))
num_2 = int(input('Please, input 2-nd number: '))
print(divide_numb(num_1, num_2))