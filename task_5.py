class Stationery:
    title = 0

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def __init__(self):
        self.name = 'Ручка'

    def draw(self):
        return 'Не стирается'


class Pencil(Stationery):
    def __init__(self):
        self.name = 'Карандаш'

    def draw(self):
        return 'Стирается'


class Handle(Stationery):
    def __init__(self):
        self.name = 'Маркер'

    def draw(self):
        return 'Пишет жирно'


pen = Pen()
pencil = Pencil()
handle = Handle()

print(pen.name + ' ' + pen.draw())
print(pencil.name + ' ' + pencil.draw())
print(handle.name + ' ' + handle.draw())
