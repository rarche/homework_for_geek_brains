
original_list = [11, 11, 11, 234, 20, 1, 1, 24, 2, 2, 33, 33, 33, 10]
new_list = [i for i in original_list if original_list.count(i) == 1]
print(new_list)
