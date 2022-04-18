'''Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
 Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.'''

'''Продолжить работу над первым заданием. Разработайте методы, которые отвечают
за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).'''

'''Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.'''


class Stock:
    number_of_printer = 0
    number_of_scanner = 0
    number_of_copier = 0

    def __init__(self, name, address, office):
        '''Инициализация данных.'''
        self.name = name
        self.address = address
        self.office = office

class Equipment(Stock):
    def __init__(self, model, price, number: int):
        '''Инициализация данных.'''
        self.model = model
        self.price = price
        self.number = number
        try:
            if type(self.number) != int:
                raise MyError('Не то вводим!')
        except MyError:
            print('Количество должно быть числом!')
            self.number = 0



class Printer(Equipment):
    def __init__(self, speed_of_print, *args):
        '''Инициализация данных.'''
        self.speed_of_print = speed_of_print
        super().__init__(*args)
        Stock.number_of_printer += self.number
        print(f'Поступило на склад {Stock.number_of_printer} единиц {self.model}')

    def release(self, number):
        '''Выдача со склада'''
        Stock.number_of_printer -= number
        print(f'Выдано со склада {number} {self.model}')
        print(f'Остаток {self.model} на складе {Stock.number_of_printer}')


class Scanner(Equipment):
    def __init__(self, resolution, *args):
        '''Инициализация данных.'''
        self.resolution = resolution
        super().__init__(*args)
        Stock.number_of_scanner += self.number
        print(f'Поступило на склад {Stock.number_of_scanner} единиц {self.model}')

    def release(self, number):
        '''Выдача со склада'''
        Stock.number_of_scanner -= number
        print(f'Выдано со склада {number} {self.model}')
        print(f'Остаток {self.model} на складе {Stock.number_of_scanner}')

class Copier(Equipment):
    def __init__(self, speed_of_copy, *args):
        '''Инициализация данных.'''
        self.speed_of_copy = speed_of_copy
        super().__init__(*args)
        Stock.number_of_copier += self.number
        print(f'Поступило на склад {Stock.number_of_copier} единиц {self.model}')

    def release(self, number):
        '''Выдача со склада'''
        Stock.number_of_copier -= number
        print(f'Выдано со склада {number} {self.model}')
        print(f'Остаток {self.model} на складе {Stock.number_of_copier}')

class MyError(Exception):
    def __init__(self, text):
        self.txt = text

sklad1 = Stock('first', 'Spb', 'Nevsky')
cop1 = Copier(1000, 'copier HP', 120, 'строка')
printer1 = Printer(120, 'printer Samsung', 200, 7)
scanner1 = Scanner('9600 dpi', 'scanner Toshiba', 105, 3)

printer1.release(5)
printer1.release(2)
cop1.release(3)
scanner1.release(1)

