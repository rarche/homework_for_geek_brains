products_list = []
please_stop_counter = 1
stop_word = ''
while stop_word != 'stop':
     name = input('Введите название товара: ')
     price = int(input('Введите цену товара: '))
     amount = int(input('Введите количество товаров: '))
     measures = input('Введите единицы исчисления: ')
     products_list.append(
         (please_stop_counter, {'name': name, 'price': price, 'amount': amount, 'measures': measures})
     )
     please_stop_counter += 1
     stop_word = input('Напишите "stop", когда товаров будет достаточно: ')

print(products_list)

dict_for_products = {}

for number, products_tuple in products_list:
    for key, value in products_tuple.items():
        if not dict_for_products.get(key):
            dict_for_products[key] = [value]
        else:
            dict_for_products[key].append(value)

for key, value in dict_for_products.items():
    dict_for_products[key] = list(set(value))

print(dict_for_products)
