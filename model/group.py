# -*- coding: utf-8 -*-

from sys import maxsize

# Конструктор класса групп
class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):  # Переопределение функции вывода значений
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):  # Переопределение функции сравнения
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
