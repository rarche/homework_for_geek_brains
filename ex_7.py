def num_fact(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
        yield fact

for count,el in enumerate(num_fact(10)):
    print(f'{count+1}. {el}')
