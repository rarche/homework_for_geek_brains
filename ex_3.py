# calendar = {'winter': (12, 1, 2),
#             'spring': (3, 4, 5),
#             'summer': (6, 7, 8),
#             'autumn': (9, 10, 11)}
#
# user_info = int(input('Введите месяц в виде числа от 1 до 12:'))
#
# for key in calendar:
#     if user_info in calendar[key]:
#         print(key)

user_info = input('Введите месяц в виде числа от 1 до 12: ')

w, sp, su, a = 'winter', 'spring', 'summer', 'autumn'

calendar = {'1' : w, '2' : w, '3' : sp, '4' : sp, '5' : sp, '6' : su, '7' : su, '8' : su, '9' : a, '10' : a, '11' : a, '12' : w}

print(calendar[user_info])

user_info = int(user_info)
calendar_list = (w, w, sp, sp, sp, su, su, su, a, a, a, w)
print(calendar_list[user_info - 1])