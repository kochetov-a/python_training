# -*- coding: utf-8 -*-

from model.group import Group

def test_delete_first_group(app):
    # Если на странице групп, нет групп
    if app.group.count_group() == 0:
        # Создаём новую группу для удаления
        app.group.create(Group(name="Group for delete"))
    # Сохранение списка групп ДО удаления
    old_groups = app.group.get_group_list()
    # Удаляем первую группу из списка
    app.group.delete_first_group()
    # Сохранение списка групп ПОСЛЕ удаления
    new_groups = app.group.get_group_list()
    # Сравнение что на одну группу стало меньше после добавления
    assert len(old_groups) - 1 == len(new_groups)