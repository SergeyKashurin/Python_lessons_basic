
__author__ = 'Кашурин Сергей Петрович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# Решение 1
# print(max(str(58375)))

# Решение 2
# x = 58375
# x_str = str(x)
# x_max = int(x_str[0])
#
# for i in x_str:
#     if x_max < int(i):
#         x_max = int(i)
# print(x_max)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# Решение 1
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# a = a + b
# b = a - b
# a = a - b
#
# print(a,b)

# Решение 2
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# a, b = b, a
#
# print(a,b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# Решение 1
import math
a = int(input("Введите A: "))
b = int(input("Введите B: "))
c = int(input("Введите C: "))

# Вычисляем дискриминант
d = (b * b) - (4 * a * c)

if d == 0:
    print("X1 %.2f" % (-b / (2 * a)))
elif d > 0:
    print("X1 %.2f" % ((-b + math.sqrt(d)) / (2 * a)))
    print("X2 %.2f" % ((-b - math.sqrt(d)) / (2 * a)))
elif d < 0:
    print("Корней нет")
