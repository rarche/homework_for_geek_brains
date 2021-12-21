from functools import reduce

dict_of_lessons = {}
with open('text_6.txt') as file:
    read = file.read()
    read = list(read.split('\n'))
    for i in read:
        one_lesson = i.split()
        list_of_numbs = []
        obj = one_lesson[0]
        obj = obj[:-1]
        for elem in one_lesson:
            only_numbs = elem.split('(')
            for el in only_numbs:
                if el.isdigit():
                    el = int(el)
                    list_of_numbs.append(el)
                    sum_of_lessons = reduce(lambda prev, next: prev+next, list_of_numbs)
                    dict_of_lessons.update({obj: sum_of_lessons})

print(dict_of_lessons)
