# -*- coding: utf-8 -*-

from model.group import Group
from random import *


# Модификация случайной группы из списка
def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:  # Если в базе данных нет групп, создаем группу
        app.group.create(Group(name="Group Test", header="Header Test", footer="Footer Test"))  # Создаём новую группу
    group = Group(name="New Group", header="New Header", footer="New Footer")  # Новые параметры заносим в переменную
    old_groups = db.get_group_list()  # Получение списка групп из БД до модификации
    index = randrange(len(old_groups))  # Получение номера случайной группы для модификации
    group.id = old_groups[index].id  # Получаем id выбранной группы
    app.group.modify_group_by_id(group.id, group)  # Модифицируем выбранную группу по id
    new_groups = db.get_group_list()  # Сохранение списка групп ПОСЛЕ модификации
    old_groups[index] = group  # Добавляем параметры в выбранную группу по index
    # Сравниваем отсортированные по ключу (id) списки групп
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:  # Включение проверки графического интерфейса при наличии ключа "--check_ui"
        # Сравниваем отсортированные по ключу (id) списки групп
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)