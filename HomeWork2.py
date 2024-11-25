# Импортируем необходимые библиотеки
from threading import Thread
from time import sleep


# Класс Knight, представляющий рыцаря
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()  # Инициализация потока
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        day = 0
        while enemies > 0:
            enemies -= self.power  # Уменьшение числа врагов
            sleep(1)  # Задержка между днями
            day += 1
            print(f'{self.name} сражается {day} день(дня)..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


# Создаем рыцарей и запускаем их в отдельных потоках
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
