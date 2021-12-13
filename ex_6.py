from itertools import count, cycle

for i in count(5):
    if i > 11:
        break
    else:
        print(i, end=' ')

print('\n')
list_of_everything = [1, 2, 3, 'l', 'k', 's', {}]

count_of_cycle = 0
for elem in cycle(list_of_everything):
    if count_of_cycle > 23:
        break
    print(elem, end=' ')
    count_of_cycle += 1
