# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year: str):
        self.__day_month_year = day_month_year

    @classmethod
    def make_int(cls, day_month_year):
        lst1 = day_month_year.split('-')
        return list(map(int, lst1))
    @staticmethod
    def validation(day_month_year: str):
        lst1 = day_month_year.split('-')
        lst2 = list(map(int, lst1))
        if 31 < lst2[0] < 1:
            return 'Неверно введен день'
        if 12 < lst2[1] < 1:
            return 'Неверно введен месяц'
        if 2100 < lst2[2] < 1:
            return 'Неверно введен год'
        else: return 'Усе в порядке'



data1 = Data('12-01-2018')

print(Data.make_int('12-01-2018'))

print(Data.validation('12-01-2018'))
