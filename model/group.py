# -*- coding: utf-8 -*-

from sys import maxsize

# Конструктор класса групп
class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # Переопределение функции вывода значений для групп
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    # Переопределение функции сравнения групп
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    # Функция возвращает максимальный id или (если он None) максимальное число
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
