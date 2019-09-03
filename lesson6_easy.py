# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Полицейский автомобиль' if self.is_police else 'Автомобиль', ' марки ', self.name, ', цвет: ',
              self.color, ' поехал со скоростью', self.speed, 'км//ч')

    def stop(self):
        print('Полицейский автомобиль' if self.is_police else 'Автомобиль', ' марки ', self.name, ', цвет: ',
              self.color, ' остановился')

    def turn(self, direction):
        print('Полицейский автомобиль' if self.is_police else 'Автомобиль', ' марки ', self.name, ', цвет: ',
              self.color, ' повернул ', direction)


TC1 = TownCar('Ford Focus',110,'Red',False)


class SportCar:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Полицейский автомобиль' if self.is_police else 'Автомобиль', ' марки ', self.name, ', цвет: ',
              self.color, ' поехал со скоростью', self.speed, 'км//ч')

    def stop(self):
        print('Полицейский автомобиль' if self.is_police else 'Автомобиль', ' марки ', self.name, ', цвет: ',
              self.color, ' остановился')

    def turn(self, direction):
        print('Полицейский автомобиль' if self.is_police else 'Автомобиль', ' марки ', self.name, ', цвет: ',
              self.color, ' повернул ', direction)


SC1 = SportCar('Chevrolet Corvette',180,'Yellow',False)


class WorkCar:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Полицейский автомобиль' if self.is_police else 'Автомобиль', ' марки ', self.name, ', цвет: ',
              self.color, ' поехал со скоростью', self.speed, 'км//ч')

    def stop(self):
        print('Полицейский автомобиль' if self.is_police else 'Автомобиль', ' марки ', self.name, ', цвет: ',
              self.color, ' остановился')

    def turn(self, direction):
        print('Полицейский автомобиль' if self.is_police else 'Автомобиль', ' марки ', self.name, ', цвет: ',
              self.color, ' повернул ', direction)


WC1 = WorkCar('Ford Transit',90,'White',False)


class PoliceCar:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(('Полицейский автомобиль' if self.is_police else 'Автомобиль'),'марки ', self.name, ', цвет: ', self.color, ' поехал со скоростью', self.speed, 'км//ч')

    def stop(self):
        print(('Полицейский автомобиль' if self.is_police else 'Автомобиль'),'марки ', self.name, ', цвет: ', self.color, ' остановился')

    def turn(self, direction):
        print(('Полицейский автомобиль' if self.is_police else 'Автомобиль'),'марки ', self.name, ', цвет: ', self.color, ' повернул ', direction)

PC1 = PoliceCar('Ford Explorer',190,'Black',True)

TC1.go()
SC1.stop()
WC1.turn('налево')
PC1.turn('направо')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        print('Автомобиль марки ', self.name, ', цвет: ',
                  self.color, ' поехал со скоростью', self.speed, 'км//ч')

    def stop(self):
        print('Автомобиль марки ', self.name, ', цвет: ',
                  self.color, ' остановился')

    def turn(self, direction):
        print('Автомобиль марки ', self.name, ', цвет: ',
                  self.color, ' повернул ', direction)


class NewTownCar(Car):

    def __init__(self, name, speed, color, is_police):
        Car.__init__(self, name, speed, color)
        self.is_police = is_police

class NewSportCar(Car):

    def __init__(self, name, speed, color, is_police):
        Car.__init__(self, name, speed, color)
        self.is_police = is_police


class NewWorkCar(Car):

    def __init__(self, name, speed, color, is_police):
        Car.__init__(self, name, speed, color)
        self.is_police = is_police


class NewPoliceCar(Car):

    def __init__(self, name, speed, color, is_police):
        Car.__init__(self, name, speed, color)
        self.is_police = is_police

    def go(self):
        print('Полицейский автомобиль марки ', self.name, ', цвет: ',
                  self.color, ' поехал со скоростью', self.speed, 'км//ч')

    def stop(self):
        print('Полицейский автомобиль марки ', self.name, ', цвет: ',
                  self.color, ' остановился')

    def turn(self, direction):
        print('Полицейский автомобиль марки ', self.name, ', цвет: ',
                  self.color, ' повернул ', direction)

TC2 = NewTownCar('Ford Focus',110,'Red',False)
SC2 = NewSportCar('Chevrolet Corvette',180,'Yellow',False)
WC2 = NewWorkCar('Ford Transit',90,'White',False)
PC2 = NewPoliceCar('Ford Explorer',190,'Black',True)

TC2.go()
SC2.stop()
WC2.turn('налево')
PC2.turn('направо')