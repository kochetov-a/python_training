# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()  # Сохранение списка групп ДО добавления
    app.group.create(group)  # Добавление новой группы
    new_groups = db.get_group_list()  # Сохранение списка групп ПОСЛЕ добавления
    old_groups.append(group)  # Добавляем параметры новой группы в список старых групп
    # Сравниваем отсортированные по ключу (id) списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
