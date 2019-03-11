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
            tmp_values, random_values = self.list_random_values_generate(tmp_values)

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
        i = 0
        tmp = []
        while i <= 5:
            rnd = randint(0, 9)
            if rnd not in tmp:
                tmp.append(rnd)
                i += 1
        return sorted(tmp)

    @staticmethod
    def list_random_values_generate(tmp_values):
        '''
        Заполнить карту неповторяющимися значениями
        :param tmp_values:
        :return:
        '''
        i = 0
        tmp = []
        while i <= 5:
            rnd = randint(0, 99)
            if rnd not in tmp and rnd not in tmp_values:
                tmp.append(rnd)
                tmp_values.append(rnd)
                i += 1
        return tmp_values, sorted(tmp)

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

    @property
    def are_you_winner(self):
        '''
        Узнаём победителя (у кого не осталось значений в карте)
        :return:
        '''
        flag = True
        for x in self._card:
            for y in x:
                if y != ' ' and y >= 0:
                    flag = False
        return flag