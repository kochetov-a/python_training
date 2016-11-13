# -*- coding: utf-8 -*-

from model.group import Group

def test_modify_group_name(app):
    # Если на странице групп, нет групп
    if app.group.count_group() == 0:
        # Создаём новую группу для модификации
        app.group.create(Group(name="Group for modify"))
    # Модифицируем первую группу из списка
    app.group.modify_first_group(Group(name="New Group"))