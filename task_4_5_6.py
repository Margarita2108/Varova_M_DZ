class WarehouseEquipment:
    warehouse_name = 'Склад 1'
    warehouse_address = 'Воронеж'


class Equipment(WarehouseEquipment):
    name = 'Equipment'
    price = 0
    quantity = 0

    def __str__(self):
        return f'{self.name}  остаток на {self.warehouse_name} {self.warehouse_address}:  ' \
               f'{self.quantity} шт на сумму {self.quantity * self.price}'

    def __sub__(self, other):
        try:
            if self.quantity < other.quantity:
                raise ValueError
            self.quantity = self.quantity - other.quantity
            print(f'Со склада переместили {self.name} ')
        except ValueError:
            print("Столько на складе нет")
            pass
        finally:
            return self.quantity

    def __add__(self, other):
        self.quantity = self.quantity + other.quantity
        print(f'На склад добавили {self.name} ')
        return self.quantity


class Printer(Equipment):
    name = 'Принтер'
    price = 2500
    colors = True

    def __init__(self, quantity):
        self.quantity = quantity


class Scanner(Equipment):
    name = 'Сканер'
    price = 2000
    colors = True

    def __init__(self, quantity):
        self.quantity = quantity


class Copier(Equipment):
    name = 'Копир'
    price = 5000
    auto_feed = False

    def __init__(self, quantity):
        self.quantity = quantity


if __name__ == '__main__':
    # На склад помещаем технику
    unit_printer = Printer(5)
    unit_scanner = Scanner(5)
    unit_copier = Copier(1)
    # Поступившие принтеры
    unit_printer_reception = Printer(3)
    # Принтеры для перемещения
    unit_printer_transfer = Printer(7)

    # перемещение позиций
    print(unit_printer)
    unit_printer - unit_printer_transfer
    print(unit_printer)
    unit_printer + unit_printer_reception
    print(unit_printer)
    unit_printer - unit_printer_transfer
    print(unit_printer)


