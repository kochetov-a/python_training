# -*- coding: utf-8 -*-

from model.group import Group
from random import randrange

# Удаление случаной группы из списка
def test_delete_some_group(app):
    if app.group.count_group() == 0:  # Если на странице групп, нет групп
        app.group.create(Group(name="GroupTest"))  # Создаём новую группу для удаления
    old_groups = app.group.get_group_list()  # Сохранение списка групп ДО удаления
    index = randrange(len(old_groups)) # Получение номера случайной группы для удаления
    app.group.delete_group_by_index(index)  # Удаляем из списка группу выбранную случаным образом
    new_groups = app.group.get_group_list()  # Сохранение списка групп ПОСЛЕ удаления
    assert len(old_groups) - 1 == len(new_groups)  # Сравнение что на одну группу стало меньше после добавления
    old_groups[index:index + 1] = []  # Удаляем выбранную группу из старого списка
    assert old_groups == new_groups  # Сравнение что списки групп равны
