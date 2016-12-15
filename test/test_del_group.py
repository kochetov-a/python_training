# -*- coding: utf-8 -*-

from model.group import Group
import random


# Удаление случаной группы из списка
def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:  # Если в базе данных нет групп, создаем группу
        app.group.create(Group(name="GroupTest"))  # Создаём новую группу для удаления
    old_groups = db.get_group_list()  # Получение списка групп из БД до удаления
    group = random.choice(old_groups)  # Выбираем случайную группу
    app.group.delete_group_by_id(group.id)  # Удаляем из списка группу выбранную случаным образом
    new_groups = db.get_group_list()  # Получение списка групп из БД после удаления
    old_groups.remove(group)  # Удаление группы из списка ДО удаления через интерфейс
    assert old_groups == new_groups  # Сравнение что списки групп равны
    if check_ui:  # Включение проверки графического интерфейса при наличии ключа --check_ui
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)