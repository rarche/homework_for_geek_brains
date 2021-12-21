with open('text_2.txt') as file:
    result = file.readlines()
    counter_of_string = 1
    for i in result:
        str(i)
        new_list = list(i.split())
        print(f'String №{counter_of_string} contains {len(new_list)} words')
        counter_of_string += 1

    print(f'Amount of strings: {len(result)}')


