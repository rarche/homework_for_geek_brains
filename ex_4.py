user_number = int(input("Введите целое положительное число: "))
max_numerum = user_number % 10
user_number = user_number // 10
while user_number > 0:
    if user_number % 10 > max_numerum:
        max_numerum = user_number % 10
    user_number = user_number // 10

print(f'Максимальная цифра в числе: {max_numerum}')
