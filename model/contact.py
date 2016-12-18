# -*- coding: utf-8 -*-

from sys import maxsize

# Конструктор класса контактов
class Contact:

    def __init__(self, first_name=None, second_name=None,
                 last_name=None, company_name=None, id=None,
                 home_phone=None, mobile_phone=None, work_phone=None,
                 secondary_phone=None, all_phones=None, address=None,
                 all_emails=None, email=None, email_2=None, email_3=None):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.company_name = company_name
        self.id = id
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones = all_phones
        self.address = address
        self.all_emails = all_emails
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3

    # Переопределение функции вывода значений для контактов
    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.first_name, self.second_name, self.last_name)

    # Переопределение функции сравнения контактов
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    # Функция возвращает максимальный id или (если он None) максимальное число
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
