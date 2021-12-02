user_string = input('Введите строку из нескольких слов, разделенных пробелом: ')
user_split = user_string.split()

count_of_str = 1

for n in user_split:
    print(f'{count_of_str}.{n[:10]}')
    count_of_str += 1
