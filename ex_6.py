distance_1 = float(input('Введите дистанцию на первый день: '))
distance_2 = float(input('Целевая дистанция: '))
amount_of_days = 1

while distance_1 < distance_2:
    distance_1 = distance_1 * 1.1
    amount_of_days += 1

print(f'Требуемое количество дней: {amount_of_days}')
