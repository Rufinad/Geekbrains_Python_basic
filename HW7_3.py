print('третье задание')

#3. Реализовать программу работы с органическими клетками,
# состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()). Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.
import re


class Cells:

    def __init__(self, number: int):
        self.__number = number

    def __add__(self, other):  # __add__(self, other) - сложение. x + y вызывает x.__add__(y)
        return self.__number + other.__number

    def __sub__(self, other):
        return  self.__number - other.__number

    def __mul__(self, other):
        return self.__number * other.__number

    def __truediv__(self, other):
        return round(self.__number / other.__number, 0)

    '''В классе необходимо реализовать метод make_order(),
     принимающий экземпляр класса и количество ячеек в ряду.
      Данный метод позволяет организовать ячейки по рядам.'''

    def make_order(self, cells_in_row):
        str1 = '*' * self.__number
        lst1 = re.findall('.'* cells_in_row, str1)
        lst1.append('*' * (self.__number % cells_in_row))
        print(lst1)
        str2 = '\n'.join(lst1)
        return str2

kletka1 = Cells(12)
kletka2 = Cells(10)
print(kletka1.make_order(5))
print(kletka1 + kletka2)
print(kletka1 - kletka2)
print(kletka1 * kletka2)
print(kletka1 / kletka2)

