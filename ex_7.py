def num_fact(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
        yield fact

for el in num_fact(10):
    print(el)
