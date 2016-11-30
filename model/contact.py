# -*- coding: utf-8 -*-

from sys import maxsize

# Конструктор класса контактов
class Contact:

    def __init__(self, first_name=None, second_name=None,
                 last_name=None, company_name=None, id=None,
                 home_phone=None, mobile_phone=None, work_phone=None,
                 secondary_phone=None):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.company_name = company_name
        self.id = id
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone

    # Переопределение функции вывода значений для контактов
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    # Переопределение функции сравнения контактов
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    # Функция возвращает максимальный id или (если он None) максимальное число
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
