class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки '

class Pen(Stationery):
    def draw(self):
        result = super().draw()
        result += 'ручкой.'
        return result

class Pencil(Stationery):
    def draw(self):
        result = super().draw()
        result += 'карандашом.'
        return result

class Handle(Stationery):
    def draw(self):
        result = super().draw()
        result += 'маркером.'
        return result

my_pen = Pen('pen')
my_pencil = Pencil('pencil')
my_handle = Handle('handle')
print(my_pen.draw())
print(my_pencil.draw())
print(my_handle.draw())