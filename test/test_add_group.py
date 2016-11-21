# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    # Сохранение списка групп ДО добавления
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Test1", header="test_header", footer="test_footer"))
    # Сохранение списка групп ПОСЛЕ добавления
    new_groups = app.group.get_group_list()
    # Сравнение что на одну группу стало больше после добавления
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    # Сохранение списка групп ДО добавления
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    # Сохранение списка групп ПОСЛЕ добавления
    new_groups = app.group.get_group_list()
    # Сравнение что на одну группу стало больше после добавления
    assert len(old_groups) + 1 == len(new_groups)