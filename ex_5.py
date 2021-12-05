def summ_of_numbers(numbers):
    '''

    :param numbers:list
    :return: int
    '''
    result = 0
    for elem in numbers:
        result += elem
    return result


numberus = list(input('Введите числа, разделенные пробелом (чтобы прекратить ввод, введите "!") :').split())

while numberus[-1] != '!':
    numberus_map = map(int, numberus)
    result = summ_of_numbers(numberus_map)
    print(result)
    numberus.extend(list(input('Введите числа, разделенные пробелом (чтобы прекратить ввод, введите "!") :').split()))

if numberus [-1] == '!':
    numberus.remove('!')
    numberus_map = map(int, numberus)
    result = summ_of_numbers(numberus_map)
    print(result)