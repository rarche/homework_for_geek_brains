gag_list = [8, 7, 6, 4, 4, 3, 2]

user_add = int(input('Введите натуральное число: '))
gag_count = gag_list.count(user_add)
n = 0
c = gag_list[n]
len_list = int(len(gag_list))
print(gag_list[-1])

if gag_count > 0:
    gag_index = gag_list.index(user_add)
    new_position = gag_count + gag_index
    gag_pos = gag_list.insert(new_position, user_add)

elif user_add > c:
    c_pos = gag_list.insert(n, user_add)

elif user_add < c:
    while user_add < c:
        n += 1
        c = gag_list[n]
        if user_add > c:
            c_pos = gag_list.insert(n, user_add)
        elif c == gag_list[len_list - 1]:
            c_pos = gag_list.append(user_add)


print(gag_list)

