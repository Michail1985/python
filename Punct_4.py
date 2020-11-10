class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'\nАвтомобиль {self.name} поехал.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул на {direction}.'

    def show_speed(self):
        return f'\nСкорость автомобиля {self.speed} км/ч.'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость автомобиля выше разрешенной! Ваша скорость:{self.speed} км/ч'
        else:
            return f'\nСкорость автомобиля {self.speed} км/ч.'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость автомобиля выше разрешенной! Ваша скорость:{self.speed} км/ч'
        else:
            return f'\nСкорость автомобиля {self.speed} км/ч.'

class PoliseCar(Car):
    pass

town = TownCar(75, 'белый', 'Лада', False)
print(town.go(), town.show_speed(), town.turn('лево'), town.stop())

sport = SportCar(210, 'чёрный', 'Шевроле', False)
print(sport.go(), sport.show_speed(), sport.turn('право'), sport.turn('лево'), sport.stop())

work = WorkCar(39, 'белый', 'Форд', False)
print(work.go(), work.show_speed(), work.turn('лево'), work.stop())

police = PoliseCar(120, 'синий', 'Хамер', True)
print(police.go(), police.show_speed(), police.turn('лево'), police.stop())