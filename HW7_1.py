print('первое задание')

class Matrix:
    def __init__(self, matrix_data: list[list]):

        """ 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
        который должен принимать данные (список списков) для формирования матрицы."""

        self.__matrix = matrix_data
        # for i in range(len(self.__matrix)):  # len() - возвращает количество строк в матрице
        #     for j in range(len(self.__matrix[i])):  # len(self.__matrix[i]) - возвращает количество элементов в строке i
        #         print(self.__matrix[i][j], end=' ')
        #     print()  # делаем переход на новую строку


    def __str__(self) -> str:  # зачем? и так все красиво

        '''Следующий   шаг — реализовать перегрузку метода __str__() для вывода
        матрицы в привычном виде.'''

        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


    def __add__(self, other):  #__add__(self, other) - сложение. x + y вызывает x.__add__(y).

        ''' Далее реализовать перегрузку метода __add__() для реализации операции
        сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.'''

        result = [[self.__matrix[i][j] + other.__matrix[i][j] for j in range
        (len(self.__matrix[0]))] for i in range(len(self.__matrix))]

        return '\n'.join(['\t'.join(map(str, line)) for line in result])

matrix_a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
matrix_b = Matrix([[11, 22, 33, 44], [55, 66, 77, 88]])

print(matrix_a)
print(matrix_b)
print(matrix_a + matrix_b)

