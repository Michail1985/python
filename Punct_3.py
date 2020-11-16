class Cell:

    def __init__(self, intcells):
        self.intcells = int(intcells)

    def __add__(self, other):
        return f'Сумма: {self.intcells + other.intcells}'

    def __sub__(self, other):
        return f'Вычитание: {self.intcells - other.intcells }' if self.intcells - other.intcells > 0\
            else 'Клеточка исчезла.'

    def __mul__(self, other):
        return f'Умножение: {self.intcells * other.intcells}'

    def __truediv__(self, other):
        return f'Деление: {int(self.intcells // other.intcells)}\nПервая клетка больше второй.'\
            if int(self.intcells // other.intcells) > 0\
            else f'Деление: {int(other.intcells // self.intcells)}\nВторая клетка больше первой.'

    def make_order(self, row):
        result = ''
        for i in range(int(self.intcells / row)):
            result += '*' * row + '\n'
        result += '*' * (self.intcells % row)
        return result

cell = Cell(23)
cell_1 = Cell(24)
print(cell)
print(cell / cell_1)
print(cell - cell_1)
print(cell.make_order(5))