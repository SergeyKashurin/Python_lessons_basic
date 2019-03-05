# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


# Решение 1
class Worker:
    '''
    Класс "Сотрудник"
    '''
    def __init__(self, data):
        '''
        Каждый работник получает строку из файла
        :param data:
        '''
        res = data.split(" ")
        if len(res) > 0:
            [name, family, salary, position, hours_norm, hours_work] = res
            self.name = name
            self.family = family
            self.salary = int(salary)
            self.position = position
            self.hours_norm = int(hours_norm)
            self.hours_work = int(hours_work)


def smart_union(main_lst, etc_lst):
    tmp = []
    for i in main_lst:
        for j in etc_lst:
            if i[1] in j[1]:
                tmp.append(i + j[2:])
                break
    return tmp


with open("data/workers", encoding="utf-8", mode="r") as tmp:
    salary_lst = [i.split() for i in tmp][1:]

with open("data/hours_of", encoding="utf-8", mode="r") as tmp:
    worked_hours_lst = [i.split() for i in tmp][1:]

union_list = smart_union(salary_lst, worked_hours_lst)

# Создаём из объединённого списка (результата работы smart_union) экземпляры класса "Worker"
workers = []
for lst in union_list:
    workers.append(Worker(" ".join(lst)))

# Рассчитываем заработную плату
for worker in workers:
    salary, hours_norm, hours_work = worker.salary, worker.hours_norm, worker.hours_work

    work = hours_work - hours_norm
    if work > 0:
        price = salary + (2 * (salary / hours_norm) * (hours_work - hours_norm))
    else:
        price = salary + (salary / hours_norm) * (hours_work - hours_norm)
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15.2f}".format(worker.name, worker.family, worker.salary, worker.position, worker.hours_norm, worker.hours_work, price))
