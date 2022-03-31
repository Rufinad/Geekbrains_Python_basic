print('первое задание')
'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль'''


first = int(input('Введите первое число '))
second = int(input('Введите второе число '))


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')


print('Частное от деления = ', div(first, second))


print('второе задание')

'''Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой'''


def user(name, surname, year, city, email, phone):
    print(f'имя: {name}, фамилия: {surname}, год рождения: {year}, город проживания: {city}, почта: {email}, телефон: {phone}')


user(name='Петр', year=1988, phone=5857934, surname='Петров', city='Питер', email='nagibator@mail.ru')


print('третье задание')
'''реализовать функцию, которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов'''

def my_func(a, b, c):
    my_list = []
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
    my_list.sort(reverse=True)
    print('Cумма наибольших двух чисел = ', my_list[0] + my_list[1])

number_1 = int(input('Введите первое число '))
number_2 = int(input('Введите второе число '))
number_3 = int(input('Введите третье число '))

my_func(number_1, number_2, number_3)


print('четвертое задание')
"""Программа принимает действительное положительное число х и целое отрицательное число у.
Выполните возведение числа х в степень у. Задание реализуйте в виде функции my_func(x,y). 
При решении задания нужно обойтись без встроенной функции возведения числа в степень"""

def my_func1(x, y):
    print(x**y)
    z = x
    for i in range(-y-1):
        x *= z
    print(1/x)


x = int(input('Введите действительное положительное число! '))
while x < 0:
    print('Положительное Карл!')
    x = int(input('Введите действительное положительное число! '))


y = int(input('Введите целое отрицательное число! '))
while y >= 0:
    print('Отрицательное Карл!')
    y = int(input('Введите целое отрицательное число! '))

my_func1(x, y)

print('пятое задание')
'''Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введеных чисел будет добавляться к уже посчитанной сумме
Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
 к полученной ранне и после этого завершить программу.'''

def sum_str(str1):
    value = 0
    while str1:
        for numb in str1.split(' '):
            if numb != 'stop':
                value += int(numb)
            else: return value
        str1 = input('Введите еще несколько чисел, либо введите stop: ')


str1 = input('Введите несколько чисел: ')

print('Итоговая сумма всех введеных чисел = ', sum_str(str1))

# Введите несколько чисел 10 12 15
# Введите еще несколько чисел, либо введите stop 10 12 15
# Введите еще несколько чисел, либо введите stop 1 stop 2 3
# Итоговая сумма всех введеных чисел =  75


print('шестое и седьмое задание')

'''Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую 
их же, но с прописной первой буквы. Например, print(int_func('text')) -> Text
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы.'''


def int_func(words):
    cap_lst = []
    lst = words.split(' ')
    for word in lst:
        cap_lst.append(word.capitalize())
    print(" ".join(cap_lst))

words = input('Введите строку из слов ')

int_func(words)