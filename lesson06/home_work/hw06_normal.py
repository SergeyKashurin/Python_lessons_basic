# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


# Решение 1
class People:
    '''
    Описание основных черт человека

    string: name          - имя
    string: surname       - фамилия
    string: patronymic    - отчество
    '''
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    @property
    def get_full_name(self):
        '''
        Ф.И.О полностью
        '''
        return '{0} {1} {2}'.format(self.surname, self.name, self.patronymic)

    @property
    def get_short_name(self):
        '''
        Ф.И.О в формате "Фамилия И.О."
        '''
        return '{0} {1} {2} '.format(self.surname, self.name[:1], self.patronymic[:1])


class Student(People):
    '''
    Описание типа "Школьник"

    string: name          - имя
    string: surname       - фамилия
    string: patronymic    - отчество
    string: student_class - класс в формате "1Б"
    list:   parents       - родители (список)
    '''
    def __init__(self, name, surname, patronymic, class_room, parents):
        People.__init__(self, name, surname, patronymic)
        self.class_room = class_room
        self.parents = parents

    @property
    def get_class_room(self):
        return self.class_room

    @property
    def get_parents(self):
        return self.parents

class Teacher(People):
    '''
    Описание типа "Предодаватель"

    string: name          - имя
    string: surname       - фамилия
    string: patronymic    - отчество
    string: student_class - класс в формате "1Б, 7А"
    string: subject       - предмет
    '''
    def __init__(self, name, surname, patronymic, class_room, subject):
        People.__init__(self, name, surname, patronymic)
        self.class_room = class_room
        self.subject = subject

    @property
    def get_classes(self):
        return self.class_room

    @property
    def get_courses(self):
        return self.subject

class Parent(People):
    '''
    Описание типа "Родитель"

    string: name          - имя
    string: surname       - фамилия
    string: patronymic    - отчество
    '''
    def __init__(self, name, surname, patronymic):
        People.__init__(self, name, surname, patronymic)


class School:
    '''
    Описание типа "Школа"

    list: teachers - список учителей
    list: students - список чащихся
    '''
    def __init__(self, teachers, students):
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        '''
        Получить полный список всех классов школы
        '''
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        '''
        Получить список всех учеников в указанном классе
        '''
        return [student.get_short_name for student in self._students if class_room == student.get_class_room]

    def get_teachers(self, class_room):
        '''
        Получить список всех Учителей, преподающих в указанном классе
        '''
        return [teacher.get_short_name for teacher in self._teachers if class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        '''
        Полная информация об учащемся
        '''
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in self._teachers if person.get_class_room in teachers.get_classes]
                lessons = [teachers.subject for teachers in self._teachers if person.get_class_room in teachers.get_classes]
                parents = person.get_parents[0].get_full_name + " \ " + person.get_parents[1].get_full_name

                return {'ФИО': student_full_name, 'Класс': person.get_class_room, 'Учителя': teachers, 'Предметы': lessons, 'Родитель': parents}


# Список преподавателей
teachers_list = [
    Teacher("Иван", "Федорович", "Павлов", "1А, 2А, 3А, 1Б, 2Б, 3Б, 1В, 2В, 3В", "Математика"),
    Teacher("Евлампий", "Акакиевич", "Федоров", "1Б, 2Б, 3Б", "Русский язык"),
    Teacher("Кондрат", "Рассолович", "Иванов", "1А, 3А, 3Б, 3В", "Информатика")]

# Список учащихся
students_list = [
    Student("Сергей", "Кашурин", "Петрович", "1А", [Parent("Пётр", "Кашурин", "Михайлович"), \
                                                    Parent("Валентина", "Кашурина", "Дмитриевна")]),

    Student("Иван", "Иванов", "Вообщетович", "1А", [Parent("Иван", "Вообщетович", "Павлович"), \
                                                    Parent("Екатерина", "Вообщетовна", "Васильевна")]),

    Student("Никита", "Васин", "Логонов", "1Б", [Parent("Василий", "Логонов", "Евлампиевич"), \
                                                    Parent("Снежанна", "Логоновна", "Раисовна")]) ]

school = School(teachers_list, students_list)

# print('Список классов школы:, '.join(school.get_all_classes()))
# print('Список 1А класса:', school.get_students('1А'))
student = school.find_student('Кашурин Сергей Петрович')
# print(student)

print('Преподаватели в 1А: {0}'.format(', '.join(school.get_teachers('1А'))))
