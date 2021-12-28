from sys import argv

if len(argv) < 4:
    print('Необходимо ввести все данные')
else:
    hours = int(argv[1])
    money_per_hour = int(argv[2])
    bonus = int(argv[3])
    result = hours * money_per_hour + bonus
    print(result)
