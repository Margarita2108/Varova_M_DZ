from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def fabric_consumption(self):
        return f'Для пошива нужно: ? ткани'


class Coat(Clothes):
    def fabric_consumption(self):
        return f"Для пошива пальто нужно: {self.param / 6.5 + 0.5:.2f} ткани"


class Costume(Clothes):
    def fabric_consumption(self):
        return f"Для пошива костюма нужно: {2 * self.param + 0.3:.2f} ткани"


if __name__ == '__main__':
    coat = Coat(60)
    costume = Costume(155)
    print(coat.fabric_consumption())
    print(costume.fabric_consumption())

