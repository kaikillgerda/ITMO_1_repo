class Car:

    def __init__(self, color='', type='', year=''):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print('Автомобиль заглушен')

    def year_assign(self):
        self.year = input('Введите год выпуска автомобиля: ')

    def type_assign(self):
        self.type = input('Введите тип автомобиля: ')

    def color_assign(self):
        self.color = input('Введите цвет автомобиля: ')

    def car_info(self):
        print('Тип кузова: ' + self.type + '\n' + 'Год выпуска: ' + self.year + '\n' + 'Цвет: ' + self.color)


vaz_2101 = Car()

Car().start()
Car().stop()
vaz_2101.year_assign()
vaz_2101.type_assign()
vaz_2101.color_assign()
vaz_2101.car_info()
