class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split('-'):
            my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= month <= 12:
            if month == 1 | 3 | 5 | 7 | 8 | 10 | 12:
                if 1 <= day <= 31:
                    return f'Дата верна'
                else:
                    return f'Не правильное число'
            elif month == 2:
                if year % 4 == 0:
                    if 1 <= day <= 29:
                        return f'Дата верна'
                    else:
                        return f'Не правильное число'
                else:
                    if 1 <= day <= 28:
                        return f'Дата верна'
                    else:
                        return f'Не правильное число'
            else:
                if 1 <= day <= 30:
                    return f'Дата верна'
                else:
                    return f'Не правильное число'
        else:
            return f'Такого месяца нет'

    def __str__(self):
        return f'Введенная дата: {self.day_month_year}'


if __name__ == '__main__':
    user_date = '29-02-2021'
    user_date_object = Data(user_date)
    user_date_list = Data.extract(user_date)
    print(user_date_object)
    print(user_date_list)
    print(user_date_object.valid(user_date_list[0], user_date_list[1], user_date_list[2]))
