print('первое задание:')
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно в программе

list1 = ['string1', 1254, 12.58, (1, 'кортеж'), {'key': 'value'}, {1, 45}]

for i in list1:
    print(type(i))

print('второе задание:')

# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов нужно использовать функцию input

list2 = []

lenlist2 = int(input('Введите сколько элементов будет в списке'))

for i in range(lenlist2):
    list2.append(input('Введите элемент списка'))
print("Исходный список: ", list2)

for i in range(0, lenlist2, 2):
    try: list2[i], list2[i+1] = list2[i+1], list2[i]
    except IndexError:
        print('последний элемент менять не будем')

print("Изменный список: ", list2)

print('третье задание')
"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень)
Напишите решения через list и dict"""

print('решение через dict')

dict1 = {
    '6': 'лето', '7': 'лето', '8': 'лето',
    '9': 'осень', '10': 'осень', '11': 'осень',
    '12': 'зима', '1': 'зима', '2': 'зима',
    '3': 'весна', '4': 'весна', '5': 'весна'
    }

month = input('Введите месяц в виде целого числа от 1 до 12: ')

print('этот месяц относится к времени года: ', dict1.get(month))

print('решение через list')

month = input('Введите месяц в виде целого числа от 1 до 12: ')

first = [3, 4, 5]
second = [6, 7, 8]
third = [9, 10, 11]
fourth = [12, 1, 2]

if int(month) in first:
    print('весна')
if int(month) in second:
    print('лето')
if int(month) in third:
    print('осень')
if int(month) in fourth:
    print('зима')


print('четвертое задание')

"""Пользователь вводит строку из нескольких слов, разделенных пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв"""

str1 = input('Введите строку из нескольких слов ')

words = str1.split(' ')
i = 1
for word in words:
    print(i, word[:10])
    i += 1

print('пятое задание')
# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них..


my_list = [7, 5, 3, 3, 2]

new = int(input('Введите новый элемент рейтинга '))

my_list.append(new)

print(sorted(my_list, reverse=True))

print('шестое задание')

# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.


nomenclature = []
number = int(input('Введите количество товаров '))

for i in range(number):
    item = input('Введите название товара ')
    price = input('Введите цену товара ')
    volume = input('Введите количество товара ')
    unit = input('Введите единицу измерения товара ')
    dict1 = {'название': item, 'цена': price, 'количество': volume, "единица измерения": unit}
    tuple1 = (i+1, dict1)
    nomenclature.append(tuple1)

print(nomenclature)
# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

items = []
for i in range(number):
    items.append(nomenclature[i][1]['название'])
prices = []
for i in range(number):
    prices.append(nomenclature[i][1]['цена'])
volumes = []
for i in range(number):
    volumes.append(nomenclature[i][1]['количество'])
units = []
for i in range(number):
    units.append(nomenclature[i][1]['единица измерения'])

new_dict = {'название': items, 'цена': prices, 'количество': volumes, "единица измерения": units}

print(new_dict)


# [(1, {'название': 'яблоко', 'цена': '100', 'количество': '10', 'единица измерения': 'кг'}),
#           (2, {'название': 'банан', 'цена': '70', 'количество': '50', 'единица измерения': 'шт'})]
# {'название': ['яблоко', 'банан'], 'цена': ['100', '70'], 'количество': ['10', '50'], 'единица измерения': ['кг', 'шт']}