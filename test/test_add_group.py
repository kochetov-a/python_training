# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list() # Сохранение списка групп ДО добавления
    group = Group(name="Test Group 1", header="test_header", footer="test_footer")  # Параметры новой группы заносим в переменную
    app.group.create(group)  # Добавление новой группы
    new_groups = app.group.get_group_list()  # Сохранение списка групп ПОСЛЕ добавления
    assert len(old_groups) + 1 == len(new_groups)  # Сравнение что на одну группу стало больше после добавления
    old_groups.append(group)  # Добавляем параметры новой группы в список старых групп
    # Сравниваем отсортированные по ключу (id) списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()  # Сохранение списка групп ДО добавления
    group = Group(name="", header="", footer="")  # Параметры новой группы заносим в переменную
    app.group.create(group) # Добавление пустой группы
    new_groups = app.group.get_group_list() # Сохранение списка групп ПОСЛЕ добавления
    assert len(old_groups) + 1 == len(new_groups)     # Сравнение что на одну группу стало больше после добавления
    old_groups.append(group)  # Добавляем параметры новой группы в список старых групп
    # Сравниваем отсортированные по ключу (id) списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)