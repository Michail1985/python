class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовкки.'

class Pen(Stationery):
    def draw(self):
        return f'Запус отрисовки {self.title}.'

class Pencil(Stationery):
    def draw(self):
        return f'Запус отрисовки {self.title}.'

class Handle(Stationery):
    def draw(self):
        return f'Запус отрисовки {self.title}.'

pen = Pen('ручой')
pencil = Pencil('карандашём')
handle = Handle('маркером')
print(f'{pen.draw()}\n{pencil.draw()}\n{handle.draw()}')