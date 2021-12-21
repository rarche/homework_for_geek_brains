from functools import reduce
import json

with open('text_7.txt') as file:
    dict_1 = {}
    dict_2 = {}
    read = file.read()
    read = list(read.split('\n'))
    medium_profit = []
    for i in read:
        comp_list = i.split()
        profit = int(comp_list[2]) - int(comp_list[3])
        dict_1.update({comp_list[0]: profit})
        if profit > 0:
            medium_profit.append(profit)
    result = (reduce(lambda prev, next: prev+next, medium_profit)) // len(medium_profit)
    dict_2.update({'average profit': result})
    print(f'Средняя прибыль компаний, работавших без убытка, равна: {result}')

    list_of_money = [dict_1, dict_2]
    print(list_of_money)
    with open('text_7.json', 'w') as file_json:
        json.dump(list_of_money, file_json)
