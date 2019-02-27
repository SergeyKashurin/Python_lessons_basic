# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Решение 1
import os

def make_dirs(count = 1):
    for dr in range(0, count):
        dir_path = os.path.join(os.getcwd(), "dir_" + str(dr + 1))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print("Такая директория уже существует")

# Удаляем директорию по маске наименования
def delete_dirs(mask = "dir_"):
    dirs = os.listdir(path=os.getcwd())

    for dr in dirs:
        if len(dr) > 4 and dr.startswith(mask):
            dir_path = os.path.join(os.getcwd(), dr)
            try:
                os.rmdir(dir_path)
            except FileExistsError:
                print("Ошибка удаления файла", dr )

make_dirs(9)
delete_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Решение 1
def show_current_dir():
    from os import walk

    for root, dirs, files in walk("."):
        if len(dirs) > 0:
            print(dirs)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# Решение 1
import shutil
shutil.copy(__file__, __file__ + "_copy.py")