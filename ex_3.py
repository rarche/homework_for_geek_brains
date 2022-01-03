class MyException(Exception):
    def __init__(self, element):
        self.element = element


list_with_numbs = []
inp_data = input('Введите следующий элемент списка: ')
while inp_data != 'stop':
    if not inp_data.isdigit():
        try:
            raise MyException('Введенный элемент должен быть числом')
        except MyException as error:
            print(error)
            inp_data = input('Введите следующий элемент списка: ')
    else:
        list_with_numbs.append(int(inp_data))
        inp_data = input('Введите следующий элемент списка: ')

print(list_with_numbs)
