user_proceeds = int(input('Введите показатель вашей выручки: '))
user_costs = int(input('Введите показатель ваших издержек: '))
result = user_proceeds - user_costs

if user_proceeds > user_costs:
    print(f'Ваша прибыль составляет: {result}\n' +
          f'Рентабельность вашей выручки составляет: {float(result// user_proceeds)}')
    number_of_workers = int(input('Введите количество сотрудников вашей фирмы: '))
    print(f'Прибыль в расчете на одного сотрудника составляет: {int(result // number_of_workers)}')

elif user_costs > user_proceeds:
    print(f'Ваш убыток составляет: {-1 * result}')
