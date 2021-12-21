from functools import reduce

with open('text_5.txt', 'w+') as file:
    file.write('11 2 32 43 5 65 7 18')
    file.seek(0)
    list_of_num = list(file.read().split())
    list_of_num = map(int, list_of_num)
    print(f'Cумма чисел в файле равна:{reduce(lambda prev,next:prev+next, list_of_num)}')

