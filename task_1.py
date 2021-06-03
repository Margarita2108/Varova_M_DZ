import time


class TrafficLight:
    def __init__(self, color='red', switching_time=7):
        self.__color = color
        self.__switching_time = switching_time

    def switch(self):
        if self.__color == 'red':
            self.__color = 'yellow'
            self.__switching_time = 2
        elif self.__color == 'yellow':
            self.__color = 'green'
            self.__switching_time = 5
        else:
            self.__color = 'red'
            self.__switching_time = 7

    def running(self, repeat=3):
        for _ in range(repeat):
            print(self.__color)
            time.sleep(self.__switching_time)
            self.switch()


example_t_l = TrafficLight()
example_t_l.running(6)

