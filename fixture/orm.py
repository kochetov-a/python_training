from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders, encoders, convert_mysql_timestamp


class ORMFixture:

    # Переменная уровня класса
    db = Database()

    # Привязка класса групп
    class ORMGroup(db.Entity):  # Привязка класса к базе даных с помощью класса Entity внутри объекта db
        _table_ = 'group_list'  # Название таблицы
        id = PrimaryKey(int, column='group_id')     # Получаем id из столбца group_id
        name = Optional(str, column='group_name')   # Получаем name из столбца group_name
        header = Optional(str, column='group_header')   # Получаем header из столбца group_header
        footer = Optional(str, column='group_footer')   # Получаем footer из столбца group_footer
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id",
                       reverse="groups", lazy=True)

    # Привязка класса контактов
    class ORMContact(db.Entity):
        _table_ = 'addressbook'  # Название таблицы
        id = PrimaryKey(int, column='id')   # Получаем id из столбца group_id
        first_name = Optional(str, column='firstname')  # Получаем first_name из столбца firstname
        last_name = Optional(str, column='lastname')    # Получаем last_name из столбца lastname
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id",
                     reverse="contacts", lazy=True)

    # Привязка к базе данных
    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        # Привязка к базе данных
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()  # Сопоставление описанных классов с полями таблиц
        # sql_debug(True)     # Включение отображения запросов к базе данных

    # Преобразование объекта в модель класса групп
    def convert_groups_to_model(self, groups):
        def convert(group):
            # Преобразование из объекта типа orm.group в объект типа group
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    # Получение списка объектов для групп
    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    # Получение списка объектов для контактов
    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    # Преобразование объекта в модель класса контактов
    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), first_name=contact.first_name, last_name=contact.last_name,
                           deprecated=str(contact.deprecated))
        return list(map(convert, contacts))

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
