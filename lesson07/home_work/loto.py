#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


# Решение 1
from random import randint


class Card:
    def __init__(self, user_name="Computer"):
        self._user_name = user_name
        self._card = self.generate_card

    @property
    def generate_card(self):
        '''
        Генерация данных для игральной карты
        :return:
        '''
        result_list = []
        tmp_values = []

        for q in range(0, 3):
            result_list.append([" " for _ in range(0, 9)])

            tmp = self.list_index_generate
            random_values = self.list_random_values_generate(tmp_values)

            i = 0
            error = ""
            while i < 5:
                rnd_value = randint(0, 99)
                if rnd_value not in tmp_values:
                    try:
                        result_list[q][tmp[i]] = random_values[i]
                        tmp_values.append(rnd_value)
                    except IndexError as err:
                        error = err.args
                    finally:
                        i += 1

        return result_list

    @property
    def list_index_generate(self):
        '''
        Получение рандомных идексов в последствии которые будут заполнены рандомными значениями из функции list_random_values_generate
        :return:
        '''
        # TODO Иногда не генерируется достаточное количество рандомных элементов, по-этому может возникать ошибка
        return list(set([randint(0, 9) for _ in range(0, 15)]))[:9]

    def list_random_values_generate(self, tmp_values):
        '''
        Заполнить карту неповторяющимися значениями
        :param tmp_values:
        :return:
        '''
        i = 0
        tmp = []
        while i <= 5:
            rnd = randint(0, 99)
            # TODO Вариант использования изменяемого объекта необходимо продумать!
            if rnd not in tmp and rnd not in tmp_values:
                tmp.append(rnd)
                i += 1
        return sorted(tmp)

    @property
    def show_card(self):
        '''
        Распечатать карту
        :return:
        '''
        print("------------ {} карточка -----------".format(self._user_name))
        for line in self._card:
            for L in line:
                print("{:3}".format(L), end=" ")
            print()
        print("--------------------------------------")

    def cross_out_number(self, number):
        """
        Зачеркнуть значение в карте
        :param number:
        :return:
        """
        self._card[number[0]][number[1]] = " "

    @property
    def get_card(self):
        '''
        Получить значение карты
        :return:
        '''
        return self._card

    def is_exist(self, number):
        '''
        Переданный аргумент есть в карте?
        :param number:
        :return:
        '''
        i = 0
        error = ""
        finder_index = -1
        while i < 3:
            try:
                finder_index = self.get_card[i].index(number)
            except ValueError as err:
                error = err.args
            if finder_index >= 0:
                return i, finder_index
            i += 1
        return -1

    @property
    def get_user_name(self):
        '''
        Получить имя текущего владельца карты
        :return:
        '''
        return self._user_name


class Chip:
    '''
    Фишки (бочонки) с цифрами
    '''
    def __init__(self):
        '''
        Заполняем список элементами от 0 до 90
        '''
        self._chips = list(range(0, 91))

    @property
    def generate(self):
        '''
        Генерируем рандомный индекс и забираем элемент по нему удаляя из списка
        '''
        yield self._chips.pop(randint(0, len(self._chips) - 1))

    @property
    def show(self):
        '''
        Отображение текущих бочонков с цифрами
        '''
        return self._chips


print("Добро пожаловать в игру == Лото ==")
print("Пожалуйста подождите, идёт инициализация игровых объектов:\n")

user_card = Card("User")
computer_card = Card()

chip = Chip()

ship_number = 0


def show_all_cards():
    user_card.show_card
    computer_card.show_card


def next_step():
    ship_number = next(chip.generate)
    print("Выпал бочонок №", ship_number)
    show_all_cards()
    return ship_number


print("\nИнициализация завершена: карточки игроков ->\n")

show_all_cards()

while True:
    user_choice = input("Для следующего броска введите 1, для выхода из игры введите Q:")

    if user_choice in ["Q", "q"]:
        break

    if user_choice == "1":
        ship_number = next_step()

        user_shot = input("Зачеркнуть бочонок на карте? Y - зачеркнуть N - продолжить")

        if user_shot in ["Y", "y"]:
            index_is_exist = user_card.is_exist(ship_number)
            if index_is_exist != -1:
                user_card.cross_out_number(index_is_exist)
                show_all_cards()
            else:
                print("Неверно! Конец игры!!!")
                break
        elif user_shot in ["N", "n"]:
            index_is_exist = user_card.is_exist(ship_number)
            if index_is_exist != -1:
                print("Номер бочёнка был в Вашей карте, Вы проиграли! Конец игры!!!")
                break
            else:
                continue
        else:
            break
