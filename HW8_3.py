#  Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#  Проверить работу исключения на реальном примере.
#  Запрашивать у пользователя данные и заполнять список необходимо только числами.
#  Класс-исключение должен контролировать типы данных элементов списка.

class MyError(Exception):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except ValueError:
                print(f"Недопустимое значение ")
                new = input('Попробовать еще раз? Y/N ')
                if new == 'Y' or new == 'y':
                    self.my_input()
                else:
                    return f'Вы вышли'



pt1 = MyError()
pt1.my_input()

