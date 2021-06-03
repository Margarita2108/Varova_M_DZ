class Car:
    speed = 0
    color = 0
    name = 0
    is_police = False

    def go(self, speed):
        self.speed = speed
        print('Поехали')

    def stop(self):
        self.speed = 0
        print('Остановка')

    def turn(self, direction):
        print(f'Поворачиваем в {direction}')

    def show_speed(self):
        print(self.speed)


class PoliceCar(Car):
    is_police = True

    def __init__(self, color, name):
        self.color = color
        self.name = name


class TownCar(Car):
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!! ')
        print(self.speed)


class WorkCar(Car):
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!! ')
        print(self.speed)


class SportCar(Car):
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name


tc = TownCar('black', 'Audi')
pc = PoliceCar('white', 'BMW')
sc = SportCar('red', 'Ford')
wc = WorkCar('blue', 'Honda')

print(f' Автомобиль {tc.name} движется со скоростью {tc.speed} км\ч')
tc.go(50)
tc.turn(direction='лес')
tc.show_speed()
tc.speed = 10000
tc.show_speed()
print(f' Автомобиль {tc.name} движется со скоростью {tc.speed} км\ч')