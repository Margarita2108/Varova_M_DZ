class DivisionNull:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    @staticmethod
    def divide_by_null(dividend, divisor):
        try:
            return dividend/divisor
        except ZeroDivisionError:
            return 'Деление на ноль недопустимо'


if __name__ == '__main__':
    print(DivisionNull.divide_by_null(100, 0))
    print(DivisionNull.divide_by_null(100, 10))
