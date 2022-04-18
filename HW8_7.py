'''Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.'''


class Complex:
    def __init__(self, real, j=0):
        self.__complex = complex(real, j)

    def __add__(self, other):  # проверка 2го числа, является ли оно комплексным числом
        if isinstance(other, Complex):
            other = other.__complex

        complex_sum = self.__complex + other
        return Complex(complex_sum.real, int(complex_sum.imag))

    def __mul__(self, other):
        if isinstance(other, Complex):
            other = other.__complex

        complex_mul = self.__complex * other
        return Complex(complex_mul.real, int(complex_mul.imag))

    def __str__(self):
        return self.__complex.__str__()




c1 = Complex(2, -3)

print(c1.__dict__)
c2 = Complex(5)
print(c2.__dict__)

print(complex(2, -3) + complex(5))
print(complex(2, -3) * complex(5))