# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


# def my_round(number, count):
#     number = (number * (10 ** count) + 0.41) // 1
#     return number / (10 ** count)


# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# Решение 1
# def lucky_ticket(ticket_number):
#     ticket_number_str = str(ticket_number)
#     ticket_number_lst = [int(i) for i in ticket_number_str]
#     if len(ticket_number_str) > 5 and (sum(ticket_number_lst[:3]) == sum(ticket_number_lst[-3::])):
#         return True
#     else:
#         return False
#
#
# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))
