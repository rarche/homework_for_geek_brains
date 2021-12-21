from functools import reduce

with open('text_3.txt') as file:
    list_of_salary = []
    read = file.read()
    read = list(read.split('\n'))
    for i in read:
        i = i.split()
        mini_list = list(i)
        if int(mini_list[1]) < 20000:
            print(mini_list[0])
        list_of_salary.append(int(mini_list[1]))

print(f'Средняя зарплата работников равна: {(reduce(lambda prev,next:prev+next, list_of_salary)) / len(read)}')
