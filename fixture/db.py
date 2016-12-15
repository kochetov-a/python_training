import mysql.connector
from model.group import Group
from model.contact import Contact


# Класс для работы с базой данных
class DbFixture():

    def __init__(self, host, name, user, password):  # Инициализация параметров подключения к БД
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True  # Отключение кэширования в базе данных

    # Получение списка групп из базы данных из таблицы "group_list"
    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:  # Пробуем ввыполнить запрос к БД
            # Получение данных групп
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    # Получение списка контактов из базы данных из таблицы "addressbook"
    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:  # Пробуем ввыполнить запрос к БД
            # Получение данных групп
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, last_name) = row
                list.append(Contact(id=str(id), first_name=first_name, last_name=last_name))
        finally:
            cursor.close()
        return list


    # Функция для разрыва соеденения с БД
    def destroy(self):
        self.connection.close()