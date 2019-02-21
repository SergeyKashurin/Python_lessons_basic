# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# Решение 1
# Добавляем информацию о количестве отработанных часов из второго списка в первый
# def smart_union(main_lst, etc_lst):
#     tmp = []
#     for i in main_lst:
#         for j in etc_lst:
#             if i[1] in j[1]:
#                 tmp.append(i + j[2:])
#                 break
#     return tmp
#
#
# with open("data/workers", encoding="utf-8", mode="r") as tmp:
#     salary_lst = [i.split() for i in tmp][1:]
#
# with open("data/hours_of", encoding="utf-8", mode="r") as tmp:
#     worked_hours_lst = [i.split() for i in tmp][1:]
#
# union_list = smart_union(salary_lst, worked_hours_lst)
#
# print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Имя", "Отчество", "Оклад 100%", "Должность", "Норма ч.", "По факту ч.", "Выплатят"))
#
# for worker in union_list:
#     salary, hours_norm, hours_work = int(worker[2]), int(worker[4]), int(worker[5])
#
#     work = hours_work - hours_norm
#     if work > 0:
#         price = salary + (2 * (salary / hours_norm) * (hours_work - hours_norm))
#     else:
#         price = salary + (salary / hours_norm) * (hours_work - hours_norm)
#     print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15.2f}".format(worker[0], worker[1], worker[2], worker[3], worker[4], worker[5], price))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

# Решение 1
# def write_file(lst, letter):
#     new_file = open("data/fruits_{}.txt".format(letter), encoding="utf-8", mode="w")
#
#     for line in lst:
#         new_file.write(line + "\n")
#     new_file.close()
#
# tmp = []
#
# with open("data/fruits.txt", encoding="utf-8", mode="r") as file:
#     sorted_lst = sorted(list(set([i.rstrip() for i in file]))[1:])
#
#     first_letter = sorted_lst[0][:1]
#
#     for x in sorted_lst:
#         if x[:1] == first_letter:
#             tmp.append(x)
#         else:
#             write_file(tmp, first_letter)
#
#             tmp = []
#
#             first_letter = x[:1]
#             tmp.append(x)
#     else:
#         write_file(tmp, first_letter)
