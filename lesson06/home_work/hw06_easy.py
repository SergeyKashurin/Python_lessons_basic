# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Решение 1
from math import sqrt
class Triangle:
    '''
    Входные данные: 3x tuple

    properties:
    triangle_sides - стороны треугольника
    square - площадь

    def:
    height - высота
    perimeter - периметр
    '''
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    @property
    def triangle_sides(self):
        '''
        Стороны треугольника
        :return:
        '''
        ab = sqrt((self.A[0] - self.B[0]) ** 2 + (self.A[1] - self.B[1]) ** 2)
        bc = sqrt((self.B[0] - self.C[0]) ** 2 + (self.B[1] - self.C[1]) ** 2)
        ac = sqrt((self.A[0] - self.C[0]) ** 2 + (self.A[1] - self.C[1]) ** 2)
        return ab, bc, ac

    @property
    def square(self):
        '''
        Площадь треугольника
        :return:
        '''
        d1 = self.A[0] - self.C[0]
        d2 = self.A[1] - self.C[1]

        d3 = self.B[0] - self.C[0]
        d4 = self.B[1] - self.C[1]

        return abs((d1 * d4) - (d3 * d2)) / 2

    def height(self, ab, bc, ac):
        '''
        Высота треугольника
        :return:
        '''
        p = (ab + bc + ac) / 2
        h1 = sqrt(p * (p - ab) * (p - bc) * (p - ac)) * 2 / ab
        h2 = sqrt(p * (p - ab) * (p - bc) * (p - ac)) * 2 / bc
        h3 = sqrt(p * (p - ab) * (p - bc) * (p - ac)) * 2 / ac
        return int(h1), int(h2), int(h3)

    def perimeter(self, ab, bc, ac):
        '''
        Периметр треугольника
        :return:
        '''
        return round(ab + bc + ac, 2)


A = [1, 3]
B = [2, -5]
C = [-8, 4]

tr = Triangle(A, B, C)

# print("Площадь треугольника", tr.square)
# print("Высота треугольника", tr.height(*(tr.triangle_sides)))
# print("Периметр треугольника", tr.perimeter(*(tr.triangle_sides)))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class IsoscelesTrapezoid:
    '''
    Входные данные: список из 4х int элементов

    def:
    является ли фигура равнобочной трапецией

    properties:
    side_length - длина стороны
    perimeter - периметр
    square - площадь
    '''
    def __init__(self, a, b, c, d):
        self.A = a
        self.B = b
        self.C = c
        self.D = d

    def side_length(self, x, y):
        '''
        Длина стороны
        :return:
        '''
        return round(sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2), 2)

    @property
    def is_trapezoid(self):
        '''
        Является ли фигура равнобочной трапецией
        :return:
        '''
        return self.side_length(self.C, self.A) == self.side_length(self.B, self.D)

    @property
    def perimeter(self):
        '''
        Периметр трапеции
        :return:
        '''
        return round(self.side_length(self.A, self.B) + self.side_length(self.B, self.C) + \
               self.side_length(self.C, self.D) + self.side_length(self.A, self.D), 2)

    @property
    def square(self):
        '''
        Площадь трапеции
        :return:
        '''

        #TODO Вынести в конструктор
        ab = self.side_length(self.A, self.B)
        cd = self.side_length(self.C, self.D)
        bc = self.side_length(self.B, self.C)
        ad = self.side_length(self.A, self.D)
        if ab == cd:
            return round(((bc + ad) / 2) * sqrt(ab ** 2 - ((bc - ad) ** 2 / (2 * (bc - ad))) ** 2), 2)
        else:
            return round(((ab + cd) / 2) * sqrt(bc ** 2 - ((ab - cd) ** 2 / (2 * (ab - cd))) ** 2), 2)


A = (-6, 0)
B = (6, 0)
C = (2, 2)
D = (-2, 2)

tp = IsoscelesTrapezoid(A, B, C, D)

# print('Дины стороны трапеции [A B]: ', tp.side_length(A, B))
# print('Дины стороны трапеции [C D]: ', tp.side_length(C, D))
# print('Дины стороны трапеции [B C]: ', tp.side_length(B, C))
# print('Дины стороны трапеции [A D]: ', tp.side_length(A, A))

# print("Является ли фигура равнобочной трапецией", tp.is_trapezoid)
# print("Периментр равнобочной трапецией", tp.perimeter)
print("Площадь равнобочной трапецией", tp.square)
