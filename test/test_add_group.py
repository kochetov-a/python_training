# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string

# Генератор тестовых данных
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# Генерация тестовых данных
data_for_group = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

@pytest.mark.parametrize("group", data_for_group, ids=[repr(x) for x in data_for_group])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()  # Сохранение списка групп ДО добавления
    app.group.create(group)  # Добавление новой группы
    assert len(old_groups) + 1 == app.group.count_group()  # Сравнение что на одну группу стало больше после добавления
    new_groups = app.group.get_group_list()  # Сохранение списка групп ПОСЛЕ добавления
    old_groups.append(group)  # Добавляем параметры новой группы в список старых групп
    # Сравниваем отсортированные по ключу (id) списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
