from random import randint

class Chip:
    '''
    Фишки (бочонки) с цифрами
    '''
    def __init__(self):
        '''
        Заполняем список элементами от 1 до 90
        '''
        self._chips = list(range(1, 91))

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