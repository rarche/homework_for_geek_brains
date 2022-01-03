class Data:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def str_to_numb(cls, str_date):
        str_date = list(str_date.split('-'))
        str_date = list(map(int, str_date))
        return f'{str_date[0]:02}.{str_date[1]:02}.{str_date[2]:04}'

    @staticmethod
    def validation(str_date):
        str_date = list(str_date.split('-'))
        str_date = list(map(int, str_date))
        if 0 < str_date[1] <= 12:
            return f'Validation is correct: {str_date[0]:02}.{str_date[1]:02}.{str_date[2]:04}'
        else:
            return "Date isn't correct"


my_date = Data('01-05-2021')
print(my_date.str_to_numb('01-05-1995'))
print(my_date.validation('01-20-1995'))
print(my_date.validation('01-01-2022'))
