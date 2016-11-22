# -*- coding: utf-8 -*-

from model.group import Group
from random import randrange

# Модификация случайной группы из списка
def test_modify_group_name(app):
    if app.group.count_group() == 0:  # Если на странице групп, нет групп
        app.group.create(Group(name="GroupTest")) # Создаём новую группу для модификации
    group = Group(name="New Group")  # Параметры заносим в переменную
    old_groups = app.group.get_group_list()  # Сохранение списка групп ДО модификации
    index = randrange(len(old_groups)) # Получение номера случайной группы для модификации
    group.id = old_groups[index].id # Сохраняем id группы которую будем модифицировать
    app.group.modify_group_by_index(index, group)  # Модифицируем случайно выбранную группу из списка
    new_groups = app.group.get_group_list()  # Сохранение списка групп ПОСЛЕ модификации
    assert len(old_groups) == len(new_groups)  # Сравнение что количество групп не изменилось после модификации
    old_groups[index] = group  # Добавляем параметры в выбранную группу
    # Сравниваем отсортированные по ключу (id) списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)