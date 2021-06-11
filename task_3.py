class ExceptionList:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите число - '))
                self.my_list.append(val)
            except ValueError:
                print(f'Вы ввели не число')
                y_or_n = input(f'Проболжить? Y')
                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                else:
                    return 'Список заполнен'
            finally:
                print(f'Итоговый список чисел- {self.my_list} \n ')


if __name__ == '__main__':
    try_except = ExceptionList()
    print(try_except.my_input())
