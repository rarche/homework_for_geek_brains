def summ_of_numbers(numbers, stop_symbol):
    '''
    give summ of numbers in list
    :param numbers:list
    :return: int
    '''
    number_list = numbers.split(' ')
    result = 0
    for elem in number_list:
        if elem == stop_symbol:
            break
        result += int(elem)
    return result

stop_symbol = '!'
sum = 0
end = False


while not end:
    numberus = (input('Введите числа, разделенные пробелом (чтобы прекратить ввод, введите "!"): '))
    sum += summ_of_numbers(numberus, stop_symbol)
    end = stop_symbol in numberus
    print(f'сумма = {sum}')