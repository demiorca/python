# Задание 1

from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0

        if self.__color[0] == 'Red' and self.__color[1] == 'Yellow' and self.__color[2] == 'Green' in self.__color:
            while i < 6: # или while True для бесконечного цикла, тогда счётчик i не нужен
                for c in self.__color[0::len(self.__color) - 1]:
                    print(c)
                    i += 1
                    if c[0]:
                        sleep(7)
                    elif c[2]:
                        sleep(5)
                    print(self.__color[1])
                    sleep(2)
        else:
            print('Нарушен порядок режимов переключения')


traffic_light = TrafficLight()
traffic_light.running()
