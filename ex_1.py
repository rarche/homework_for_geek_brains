from sys import argv
hours = int(argv[1])
money_per_hour = int(argv[2])
bonus = int(argv[3])
result = hours * money_per_hour + bonus
print(result)
