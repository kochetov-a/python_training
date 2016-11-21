# -*- coding: utf-8 -*-

from model.group import Group

def test_modify_group_name(app):
    # Если на странице групп, нет групп
    if app.group.count_group() == 0:
        # Создаём новую группу для модификации
        app.group.create(Group(name="Group for modify"))
    # Сохранение списка групп ДО модификации
    old_groups = app.group.get_group_list()
    # Модифицируем первую группу из списка
    app.group.modify_first_group(Group(name="New Group"))
    # Сохранение списка групп ПОСЛЕ модификации
    new_groups = app.group.get_group_list()
    # Сравнение что количество групп не изменилось после модификации
    assert len(old_groups) == len(new_groups)