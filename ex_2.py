class MyException(Exception):
    def __init__(self, text):
        self.text = text

try:
    num_1 = int(input('Введите делимое: '))
    num_2 = int(input('Введите делитель: '))
    if num_2 != 0:
        print(f'{num_1 / num_2}')
    else:
        raise MyException('Нельзя делить на ноль')
except MyException as error:
    print(error)