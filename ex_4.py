class Storage:
    def __init__(self, storage=None):
        if not storage:
            storage = {}
        self.storage = storage

    def __str__(self):
        return f'{self.storage}'

    def add_tech(self, tech, count):
        result = self.storage.get(tech.name_of_tech, None)
        if result:
            self.storage[tech.name_of_tech] += count
        else:
            self.storage.update({tech.name_of_tech: count})

    def give_tech(self, tech):
        result = self.storage.get(tech.name_of_tech, None)
        if result:
            self.storage[tech.name_of_tech] -= 1
            return True
        else:
            return False


class Company:
    def __init__(self, name):
        self.name = name


class Administration(Company):
    def __init__(self, name, storage, tech_list=None):
        super(Administration, self).__init__(name)
        if not tech_list:
            tech_list = []
        self.tech_list = tech_list
        self.storage = storage
        if type(name) != str:
            print(f'\033[0;31;40m {Administration.__name__}, {name} - если видите данное сообщение, переназначьте значение "name" на число."\033[0;0m')

    def get_tech(self, tech):
        gt_tech = self.storage.give_tech(tech)
        if gt_tech:
            self.tech_list.append(tech)
        else:
            print('Storage do not have this tech')

    def __str__(self):
        return f'{self.tech_list}'


class OrgTech:
    def __init__(self, name, country, cost):
        self.name = name
        self.country = country
        self.cost = cost
        if type(cost) != int:
            print(f'\033[0;31;40m {self} - если видите данное сообщение, переназначьте значение "сost" на число."\033[0;0m')

    @property
    def name_of_tech(self):
        return f'{self.name} {self.country}'

    def __repr__(self):
        return f'{self.name} {self.country}'


class Printer(OrgTech):
    def __init__(self, name, country, cost, colors):
        super(Printer, self).__init__(name, country, cost)
        self.colors = colors


class Scaner(OrgTech):
    def __init__(self, name, country, cost, paper_size, speed):
        super(Scaner, self).__init__(name, country, cost)
        self.paper_size = paper_size
        self.speed = speed


class Xerox(OrgTech):
    def __init__(self, name, country, cost, paper_size, amount_of_paper):
        super(Xerox, self).__init__(name, country, cost)
        self.paper_size = paper_size
        self.amount_of_paper = amount_of_paper


printer_1 = Printer('printer', 'Germany', '10000', 2)
printer_2 = Printer('printer', 'Germany', 15000, 3)
scaner = Scaner('scaner', 'China', 5000, 'A4', 10)
xerox = Xerox('xerox', 'USA', 20000, 'A4', 15)
my_storage = Storage()
my_admin = Administration(123, my_storage)

print('Step 1')
my_storage.add_tech(printer_1, 3)
my_storage.add_tech(printer_2, 1)
print(my_storage)

print('Step 2')
my_storage.add_tech(scaner, 2)
my_storage.add_tech(xerox, 1)
print(my_storage)

print('Step 3')
my_admin.get_tech(tech=xerox)
print(my_admin)
print(my_storage)

print('Step 4')
my_admin.get_tech(tech=xerox)
print(my_storage)
my_admin.get_tech(tech=printer_2)
print(my_admin)
print(my_storage)
