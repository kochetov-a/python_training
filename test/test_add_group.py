# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()  # Получение списка групп из БД до добавления новой группы
    app.group.create(group)  # Добавление новой группы
    new_groups = db.get_group_list()  # Получение списка групп из БД после добавления новой группы
    old_groups.append(group)  # Добавляем параметры новой группы в список старых групп
    # Сравниваем отсортированные по ключу (id) списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:  # Включение проверки графического интерфейса при наличии ключа "--check_ui"
        # Сравниваем отсортированные по ключу (id) списки групп
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)