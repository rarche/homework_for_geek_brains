from functools import reduce

list_of_number = list(range(100, 1001))
print(reduce(lambda prev, cur: prev * cur, [i for i in list_of_number if i % 2 == 0]))
