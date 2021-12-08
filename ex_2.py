def person_description(name, second_name, birth_date, city, mail, phone_number):
    """
    Put all information about person in one string
    :param kwargs: tuple
    :return: tuple
    """
    return f'{name} {second_name} {birth_date} {city} {mail} {phone_number}'

name = input('Input your name: ')
second_name = input('Input your second name: ')
birth_date = input('Input your birth date: ')
city = input('Input city, where are you living right now: ')
mail = input('Input your @mail: ')
phone_number = int(input('Input your phone number (in one number): '))
print(person_description(name=name, second_name=second_name, birth_date=birth_date, city=city, mail=mail, phone_number=phone_number))



