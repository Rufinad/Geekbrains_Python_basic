from functools import reduce
print('Задание первое')
"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
Используйте в нем формулу (выработка в часах*ставка в час) + премия.
Во время выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами"""

prod = input('Введите выработку ')
bid = input('Введите ставку ')
prem = input('Введите премию ')

salary = int(prod)*int(bid) + int(prem)
print(salary)

print('Задание второе')
"""Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыущего"""

lst1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]  # результат [12, 44, 4, 10, 78, 123]

def bigger(lst):
    new_list = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            new_list.append(lst[i])
        i += 1
    return new_list

print(bigger(lst1))

print('Задание третье')

'''Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задачу в 1 строку'''

print([x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0])

print('Задание четвертое')

'''Представлен список чисел. Определите элементы списка, не имеющие повторений.
 Сформируйте итоговый массив чисел, соответствующих требованию.
  Элементы выведите в порядке их следования в исходном списке.
  Для выполнения обязательно используйте генератор'''

def unique(lst):
    return [x for x in lst if lst.count(x) == 1]
lst4 = [1,2,3,4,4,6,31,31,5,45,43,43,435]

print(unique(lst4))

print('Задание пятое')

'''Реализовать формирование списка, используя функцию range и возможности генератора.
 В список должны войти четные числа от 100 по 1000.
 Нужно получить результат вычисления произвдения всех элементов списка '''


mult5 = reduce(lambda a, b: a*b, [x for x in range(100, 1001, 2)])

print(mult5)

print('Задание шестое')

'''Реализовать 2 небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного
итератор, повторяющий элементы некоторого списка, определенного заранее.'''
from itertools import cycle

lst6 = [x for x in range(3, 11)]
iter1 = iter(lst6)

i = lst6[0]
while i < lst6[-1]:
    i = next(iter1)
    print(i, end=' ')

print('----------')


iter2 = iter(cycle(lst6))
lst6_cycle = []
i = lst6[0]
while lst6_cycle.count(i) <= 2:
    i = next(iter2)
    lst6_cycle.append(i)

print(lst6_cycle)


print('Задание седьмое')
'''Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное занчение. При вызове функции должен создаваться объект-итератор.'''

def fact(n):
    yield reduce(lambda a, b: a * b, [x for x in range(1, n+1)])

n = 8

for el in fact(n):
    print(el)

# import math
#
# def fact(n):
#     l = [i for i in range(1, n + 1)]
#     for el in l:
#         yield math.factorial(el)
# g = fact(8)
# for el in g:
#     print(el)