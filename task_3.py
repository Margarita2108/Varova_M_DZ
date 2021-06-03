class Worker:
    name = 'Иванов'
    surname = 'Иван'
    position = 'наш работник'
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def __init__(self, name, surname, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        name_worker = self.name + '  ' + self.surname
        return name_worker

    def get_total_income(self):
        income = self._income['wage'] + self._income['bonus']
        return income


position_worker = Position('Маргарита', 'Варова', 1000, 3250)

print(position_worker.get_full_name())
print(position_worker.get_total_income())
