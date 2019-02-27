# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# Решение 1
import os
import sys
import shutil

print('sys.argv = ', sys.argv)

current_dir = os.getcwd()


def print_main_menu():
    print("help - получение справки",
            "mkdir <dir_name> - создание директории",
            'cp <file_name> - создает копию указанного файла',
            'rm <file_name> - удаляет указанный файл',
            'cd <full_path or relative_path> - меняет текущую директорию на указанную',
            'ls - отображение полного пути текущей директории',
            "ping - тестовый ключ", sep="\n")


# Тест
def ping():
    print("test")


# Создаём папку
def make_dir():
    if not dir_name:
        print("[Ошибка] укажите имя директории вторым параметром")
        return
    dir_path = os.path.join(current_dir, dir_name)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print("Невозможно создать")
    else:
        print("Успешно создано")


# Удаляем файл
def remove_file():
    if not dir_name:
        print("[Ошибка] укажите имя файла вторым параметром")
        return

    file_path = os.path.join(current_dir, dir_name)
    if os.path.exists(file_path):
        answer = input("Вы действительно хотите удалить этот файл? [Д/Н]")
        if answer.lower() in ["д", "Д"]:
            os.remove(file_path)
            print('Успешно удалено')


# Копируем файл
def copy_file():
    if not dir_name:
        print("Укажите имя файла вторым параметром")
        return
    shutil.copy(__file__, __file__ + "_copy.py")


# Меняет текущую директорию на указанную
def change_dir():
    if not dir_name:
        print("[Ошибка] укажите имя директории вторым параметром")
        return
    global current_dir
    new_dir = dir_name if os.path.isabs(dir_name) else os.path.normpath(os.path.join(current_dir, dir_name))
    if os.path.exists(new_dir):
        current_dir = new_dir
        print("Успешно изменено")
    else:
        print("Невозможно изменить")


def show_current_dir():
    print(current_dir)


do = {
    "help": print_main_menu,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": show_current_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
