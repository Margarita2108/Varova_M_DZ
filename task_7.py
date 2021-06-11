class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.y * other.x + self.x * other.y} * i'

    def __str__(self):
        return f'z = {self.x} + {self.y} * i'


if __name__ == '__main__':
    numbers_1 = ComplexNumber(1, -2)
    numbers_2 = ComplexNumber(3, 4)
    print(numbers_1)
    print(numbers_2)
    print(numbers_1 + numbers_2)
    print(numbers_1 * numbers_2)
