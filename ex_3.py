class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        result = list(self._income.values())
        return int(result[0]) + int(result[1])


my_worker = Position('Billy', 'Harrington', 'boss', 300, 5)
print(my_worker.name)
print(my_worker.surname)
print(my_worker.position)
print(my_worker._income)
print(my_worker.get_full_name())
print(my_worker.get_total_income())
