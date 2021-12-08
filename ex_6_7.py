def func_letter (letters):
    result = letters.title()
    return result

print(func_letter(input('Введите слово из маленьких латинских букв: ')))

letters_list = (input('Введите строку из слов, состоящих из маленьких латинских букв: ').split())
for elem in letters_list:
    print(func_letter(elem), end=' ')