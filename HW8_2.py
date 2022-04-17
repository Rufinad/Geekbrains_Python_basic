'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.'''

class Del_0(Exception):
    def __init__(self, del1, del2):
        self.__del1 = del1
        self.__del2 = del2

    def control(del1, del2):
        try: return del1 / del2
        except ZeroDivisionError:
            return 'не дели на ноль!'

print(Del_0.control(10, 0))