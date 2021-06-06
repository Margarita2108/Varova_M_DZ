class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return sub if sub > 0 else 'Меньше 0'

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, column):
        for position in range(self.quantity):
            if (position+1) % column == 0:
                print('*')
            else:
                print('*', end='')
        return ''


if __name__ == '__main__':
    cell_1 = Cell(24)
    cell_2 = Cell(22)
    print(cell_1 + cell_2)
    print(cell_1 - cell_2)
    print(cell_1 / cell_2)
    print(cell_1 * cell_2)
    print(cell_1.make_order(5))
