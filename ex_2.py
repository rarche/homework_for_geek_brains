new_list = []
info = input('Введите элемент списка, который вы желаете внести, когда элементов будет достаточно, введите "стоп": ')
while info != 'стоп':
    new_list.append(info)
    info = input('Введите элемент списка, который вы желаете внести, когда элементов будет достаточно, введите "стоп": ')
num_index_1 = 0
num_index_2 = 1

for item in new_list:
        new_list[num_index_1], new_list[num_index_2] = new_list[num_index_2], new_list[num_index_1]
        if ((num_index_2 + 2) < len(new_list)):
            num_index_1 += 2
            num_index_2 += 2
        else: break


print(new_list)


