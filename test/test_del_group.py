# -*- coding: utf-8 -*-

from model.group import Group

def test_delete_first_group(app):
    if app.group.count_group() == 0:  # Если на странице групп, нет групп
        app.group.create(Group(name="GroupTest"))  # Создаём новую группу для удаления
    old_groups = app.group.get_group_list()  # Сохранение списка групп ДО удаления
    app.group.delete_first_group()  # Удаляем первую группу из списка
    new_groups = app.group.get_group_list()  # Сохранение списка групп ПОСЛЕ удаления
    assert len(old_groups) - 1 == len(new_groups)  # Сравнение что на одну группу стало меньше после добавления
    old_groups[0:1] = []  # Удаляем первую группу из старого списка
    assert old_groups == new_groups # Сравнение что списки групп равны
