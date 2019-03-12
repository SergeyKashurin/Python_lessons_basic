
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import urllib.request
import os
import sqlite3
import datetime
import json


class DB:
    def __init__(self, db_name="weather.db"):
        self._db_name = db_name

    @property
    def is_exist(self):
        '''
        Проверяем наличие файла базы данных
        :return:
        '''
        return os.path.isfile(self._db_name)

    @property
    def create_db(self):
        '''
        Создаём базу данных пустышку
        :return:
        '''
        conn = sqlite3.connect(self._db_name)
        conn.close()

        with sqlite3.connect(self._db_name) as conn:
            conn.execute("""
                create table weather_information (
                    id_town        INTEGER PRIMARY KEY,
                    town           VARCHAR(255),
                    calendar_date  DATE,
                    degree         INTEGER,
                    id_weather     INTEGER
                ); """)


    def insert_or_replace_db(self):
        #conn = sqlite3.connect(self._db_name)

        #conn.row_factory = sqlite3.Row

        #cur = conn.cursor()
        # cur.execute("insert or replace into weather_information (id_town, town, calendar_date, degree, id_weather) values ( \
        #     (select id_town from weather_information where town = 'Nalchik'), 'Nalchik', 5, 6")

        #conn.close()
        # for row in cur.fetchall():
        #     print(row)
        #     name, description, deadline = row
        #     print(name, description, deadline)
        pass


    def select_information_from_db_for_test(self):
        #TODO SELECT for test!
        conn = sqlite3.connect(self._db_name)
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()
        cur.execute("select * from weather_information where id_town = 523523")
        for row in cur.fetchall():
            print(row)
            town, calendar_date, degree = row
            print(town, calendar_date, degree)

    def insert_information_from_db_for_test(self):
        #TODO INSERT for test!
        conn = sqlite3.connect(self._db_name)
        conn.execute("""
            insert into weather_information (id_town, town, calendar_date, degree, id_weather) VALUES (?,?,?,?,?)""", (
                523523,
                'Nalchik',
                datetime.date.today(),
                25,
                11,
            )
        )


class JsonReader:
    def __init__(self, file_name="city.list.json"):
        self._file_name = file_name

    @property
    def is_exist(self):
        '''
        Проверяем наличие файла с данными
        :return:
        '''
        return os.path.isfile(self._file_name)

    def get_countries(self):
        '''
        Читаем страны из файла и делаем список состоящим из уникальных элементов
        :return:
        '''
        uniq = []
        with open(self._file_name, mode="r", encoding="UTF-8") as json_file:
            data = json.load(json_file)
            for p in data:
                uniq.append(p['country'])
        return sorted(set(uniq))[1:]


class Weather:
    def __init__(self, country="RU"):
        self._country = country

    @property
    def get_country(self):
        return self._country


class WeatherOnline(Weather):
    def __init__(self, country="RU"):
        Weather.__init__(self)

        self._country = country
        self._appid = "a0676fe489771bc8199bdf536f08ec11"

    @property
    def get_weather_online(self):
        return urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?id=523523&units=metric&appid={}".format(self._appid))


#1 (Если нет БД, создаём её)
db = DB()
if not db.is_exist:
    db.create_db


#2 (Читаем с файла список стран)
# json_obj = JsonReader()
# if json_obj.is_exist:
#     print("Список стран:")
#     print(json_obj.get_countries())


#3 Скачивание погоды для выбранного города
weather_online = WeatherOnline()
#print(set(weather_online.get_weather_online))


db.insert_information_from_db_for_test()
db.select_information_from_db_for_test()