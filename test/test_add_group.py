# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()  # Сохранение списка групп ДО добавления
    app.group.create(group)  # Добавление новой группы
    assert len(old_groups) + 1 == app.group.count_group()  # Сравнение что на одну группу стало больше после добавления
    new_groups = app.group.get_group_list()  # Сохранение списка групп ПОСЛЕ добавления
    old_groups.append(group)  # Добавляем параметры новой группы в список старых групп
    # Сравниваем отсортированные по ключу (id) списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
