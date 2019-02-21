# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


# Решение 1
# def fibonacci(n, m):
#     start = n
#     lst = [i for i in range(n, m + 3)]
#     while start < m:
#         lst[start + 2] = lst[start] + lst[start + 1]
#         start += 1
#     print(lst)


# fibonacci(1, 10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(origin_list):
#     for i in range(len(origin_list) - 1):
#         for j in range(len(origin_list) - i - 1):
#             if origin_list[j] > origin_list[j + 1]:
#                 origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
#     print(origin_list)


# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# def unclass_filter(func, value):
#     f = func
#     return f(value)


# hlp = [0, 50, 100, -1, 9, 4]
# print(unclass_filter(min, hlp))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# A = {"x1": 2, "y1": -1}
# B = {"x2": 5, "y2": -3}
#
# C = {"x3": -2, "y3": 11}
# D = {"x4": -5, "y4": 13}
#
# ifEdgeParallelogram = False
# if (A["y1"] - D["y4"] == B["y2"] - C["y3"]) and (B["x2"] - A["x1"] == C["x3"] - D["x4"]):
#     ifEdgeParallelogram = True
#
# print(ifEdgeParallelogram)
