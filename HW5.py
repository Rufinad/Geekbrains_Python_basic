import  re
import json

print('Первое задание')

'''Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных будет свидетельствовать пустая строка.'''

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        text = input('Введите название файла ')
        f.write(text + '\n')  # заголовок
        while text:
            text = input('Введите новую строку ')
            f.write(text + '\n')


# create_file('HW5_1.txt')

print('Второе задание')

'''2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
 выполнить подсчёт строк и слов в каждой строке.'''

def write_file(name, text=None):
    with open(name, 'a', encoding='utf-8') as f:  # открываем файл на дозапись
        text = input('Введите строку ')
        f.write('\n' + text + '\n')  # заголовок
        while text:
            text = input('Введите новую строку ')
            f.write(text + '\n')

def count_line(name):
    # считаем количество строк в файле
    with open(name, 'r', encoding='utf-8') as f: # открываем файл на чтение
        return sum(1 for line in open(name))

def count_symbol_line(name):
    # считаем количество символов построчно в файле
    with open(name, "r") as file:
        for line in file:
            print(len(line))



# write_file('HW5_2.txt')
# print(count_line('HW5_2.txt'))
# count_symbol_line('HW5_2.txt')

print('третье задание')
'''3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.'''

def write_personal_file(name):
    with open(name, 'r+', encoding='utf-8') as file:  # открываем файл на  чтение и дозапись
        file.seek(0, 2)
        new = int(input('Если хотите ввести нового сотрудника нажмите 1, если нет то 0 '))
        while new:  # записываем сотрудников и их оклады
            surname = input('Введите фамилию сотрудника ')
            salary = int(input('Введите оклад сотрудника '))
            file.write(f'{surname}  {salary}' + '\n')
            new = int(input('для завершения введения нажмите 0, для продолжения 1 '))
        #  print(file.readlines())
    x = open(name, 'r').readlines()  # ['Sasha  10000\n', 'Pasha  20000\n', 'Dima  30000\n', 'John  20000\n', 'fedy  10000\n', 'Ivan  30000\n']
    sotr = []
    for el in x:
        sotr.append(el.split(sep=None))
    # print(sotr)  # [['Sasha', '10000'], ['Pasha', '20000'], ['Dima', '30000'], ['John', '20000'], ['fedy', '10000'], ['Ivan', '30000']]
    for i in range(len(sotr)):
        if int(sotr[i][1]) < 20000:
            print(f'У {sotr[i][0]} оклад меньше 20000')  # вывод тех у кого меньше 20000
    sum = 0
    for i in range(len(sotr)):
        sum += int(sotr[i][1])
    print(sum/len(sotr))

# write_personal_file('HW5_3.txt')

print('четвертое задание')

from translate import Translator
'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

def open_swap_figures(name, name_new):
    with open(name, 'r', encoding='utf-8') as file:
        rus = []
        for line in file:
            rus.append(line.split(sep=None, maxsplit=1))
        print(rus)  # [['One', '— 1\n'], ['Two', '— 2\n'], ['Three', '— 3\n'], ['Four', '— 4']]
        for i in range(len(rus)):
            rus[i][0] = perevod.translate(rus[i][0]) # переводим вложенный список во вложенные строки
            rus[i] = " ".join(rus[i])  # ['Один — 1\n', 'Два — 2\n', 'Три — 3\n', 'Четыре — 4']
        rus = ''.join(rus)  # переводим исходный список в строки
        print(rus)
        with open(name_new, 'w', encoding='utf-8') as new_file:
             new_file.write(rus)


perevod = Translator(from_lang="english", to_lang="russian")
translation = perevod.translate("One")

# open_swap_figures('HW5_4.txt', 'HW5_4_2.txt')

print('пятое задание')
'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить её на экран.'''

def create_file_with_numbers(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        text = input('Введите первое число ')
        f.write(text + ' ')  # заголовок
        while text:
            text = input('Введите новое число, чтобы прекратить ввод нажмите Enter ')
            f.write(text + ' ')
    with open(name, 'r', encoding='utf-8') as f2:
        numbs = f2.read().split(sep=None)  # ['100', '2131', '123']
        print(sum(map(int, numbs)))

# create_file_with_numbers('HW5_5.txt')

'''6. Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''

def read_file_with_subject(name):
    with open(name, 'r', encoding='utf-8') as f:
        dict6 = {}
        for line in f:
            a = line.split(':', maxsplit=1)  # ['предмет', ' 12(л), 32(лаб), 55(пр)\n']
            lesson = (re.findall(r'\d+', a[1]))  # во втором элементе находим все цифры
            lesson = sum([int(x) for x in lesson])  # тк цифры вернулись в виде списка из строк делаем их числами и находим сумму
            dict6.update({a[0]: lesson})  # Добавляем название предмета в словарь в виде ключа а занятия в виде значения
    print(dict6)

# read_file_with_subject('HW5_6.txt')

# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

def read_file_income(name):
    with open(name, 'r', encoding='utf-8') as f:
        final = []
        averege = []
        dict7_1 = {}
        dict7_2 = {}
        for line in f:
            income = re.findall(r'\d+', line)  # в каждой строке находим все цифры
            org = (re.findall(r'^\w+', line))  # в каждой строке находим первое слово = название организации
            org = ''.join(org)  # из списка делаем строку
            income = int(income[0]) - int(income[1])
            dict7_1[org] = income
            if income > 0:
                averege.append(income)
        dict7_2['averege_profit'] = round(sum(averege)/len(averege), 2)
        final.append(dict7_1), final.append(dict7_2)
    print(final)
    with open('data.txt', 'w') as outfile:
        json.dump(final, outfile)

    # print(dict6)

# read_file_income('HW5_7.txt')

