class Road:
    def __init__(self, length=20, width=3):
        self._length = length
        self._width = width

    def calculation_weight(self, depth=3, weight=25):
        total_weight = self._length * self._width * depth * weight / 1000
        return total_weight


road_1 = Road(50, 4)
print(f'{road_1.calculation_weight(4, 30)} т')
