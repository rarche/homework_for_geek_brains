dict = {'One':'один', 'Two':'два','Three':'три','Four':'четыре'}
with open('text_4.txt') as file:
    read = file.read()
    read = list(read.split('\n'))
    for i in read:
        result = i.split()
        if result[0] in dict.keys():
            result[0] = dict[result[0]]
            result = (' '.join(result))
            print(result)
        with open('text_4_out.txt', 'a') as file_1:
            file_1.write(f'{result} \n')


