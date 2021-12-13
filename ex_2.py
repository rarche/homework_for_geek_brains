original_list = [10, 20, 5, 5, 1, 50, 4, 3, 10, 2, 2, 5]
new_list = [original_list[i + 1] for i in range(len(original_list) - 1) if original_list[i+1] > original_list[i]]
print(new_list)
