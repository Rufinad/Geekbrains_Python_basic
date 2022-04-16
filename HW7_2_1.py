print('второе задание')
# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, param):
        self.__name = name
        self.__param = param
    # @abstractmethod
    def expense(self):
        pass

class Coat(Clothes):
    def __init__(self, *args):
        super().__init__(*args)  # наследуем параметры родительского класса
    @property
    def expense(self):
        return round((self._Clothes__param / 6.5 + 0.5), 2)



class Suit(Clothes):
    def __init__(self, *args):
        super().__init__(*args)  # наследуем параметры родительского класса
    @property
    def expense(self):
        return round((self._Clothes__param * 2 + 0.3), 2)

Palto = Coat(176, 11)

Costum = Suit(25, 11)


print(Palto.expense)
print(Costum.expense)
