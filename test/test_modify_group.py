# -*- coding: utf-8 -*-

from model.group import Group

def test_modify_group_name(app):
    if app.group.count_group() == 0: # Если на странице групп, нет групп
        app.group.create(Group(name="Group for modify")) # Создаём новую группу для модификации
    app.group.modify_first_group(Group(name="New Group")) # Модифицируем первую группу из списка