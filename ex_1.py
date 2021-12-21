with open('text_1.txt', 'w') as file:
    result = input('Input something (or just press ENTER to finish): ')
    while len(result) != 0:
        file.write(f'{result} \n')
        result = input('Input something (or just press ENTER to finish): ')

