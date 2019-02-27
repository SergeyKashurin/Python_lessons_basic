# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

# Решение 1
import os
import sys
import hw05_easy as hwork


# Дополнительные функции
def print_main_menu():
    print(
        "1. Перейти в папку",
        "2. Просмотреть содержимое текущей папки",
        "3. Удалить папку",
        "4. Создать папку",
        "",
        "5. Показать главное меню ещё раз",
        "Q. Выход из OS",
        sep="\n")

		
# Функция смены рабочего каталога
def goto_dir():
    dir_name = input("Введите наименование папки:")

    try:
        os.chdir(os.path.join(os.getcwd(), dir_name))
    except:
        print("Невозможно перейти")
    else:
        print("Успешно перешел")
        print("Текущая  = ", os.getcwd())

		
# Функция просмотра содержимого текущей папки
def show_current_dir():
    from os import walk

    for root, dirs, files in walk("."):
        print(files)

		
# Удаляем директорию по маске наименования
def delete_dir():
    usr = input("Введите наименование папки: ")
    dirs = os.listdir(path=os.getcwd())

    for dr in dirs:
        if dr == usr:
            dir_path = os.path.join(os.getcwd(), dr)
            try:
                os.rmdir(dir_path)
            except FileExistsError:
                print("Невозможно удалить")
    else:
        print("Успешно удалено")

		
# Создаём папку
def make_dirs():
    usr = input("Введите наименование папки: ")
    try:
        os.mkdir(usr)
    except FileExistsError:
        print("Невозможно создать")
    else:
        print("Успешно создано")

# Можно использовать функции с модуля hw05_easy, но ТЗ этого д/з не позволяет так сделать
do = {
    "1": goto_dir,
    "2": show_current_dir,
    "3": delete_dir,
    "4": make_dirs,
    "5": print_main_menu,
}

print("Поиск необходимой мощности для запуска...")
print("Папка OS v 0.0.0.1 (SuperAlpha C2019). Добро пожаловать!\n")


print("Вот что я умею:")

print_main_menu()

while True:
    key = input()

    if do.get(key) or key == 'q':
        if key == 'q':
            sys.exit()

        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ 5 для получения справки")
