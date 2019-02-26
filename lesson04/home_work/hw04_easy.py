# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# Решение 1
# import random
#
# lst = [random.randrange(0, 10) for _ in range(5)]
# print("Исходный список: ", lst)
#
#
# def square_my_lst(loc_lst):
#     return [i * i for i in loc_lst]
#
#
# print("[DEF] Получившийся список элементов в квадрате: ", square_my_lst(lst))
#
# Решение 2
# # TODO
# print("[LMD] Получившийся список элементов в квадрате: ", (lambda x: x * x for x in lst))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# Решение 1
# fruits_lst1 = ["Apple", "Banana", "Apricot", "Grapes"]
# fruits_lst2 = ["Apple", "Fig", "Apricot", "Melon"]
#
# result_lst = list(set(fruits_lst1) & set(fruits_lst2))
#
# print(result_lst)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# Решение 1
from random import randrange

lst_sample = [randrange(-50, 50) for _ in range(15)]
print("Исходный список ", lst_sample)

finally_lst = [i for i in lst_sample if i > 0 and i % 3 == 0 and i % 4 != 0]
print("Результирующий список ", finally_lst)
