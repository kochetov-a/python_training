# -*- coding: utf-8 -*-

from model.group import Group

def test_delete_first_group(app):
    # Если на странице групп, нет групп
    if app.group.count_group() == 0:
        # Создаём новую группу для удаления
        app.group.create(Group(name="Group for delete"))
    # Удаляем первую группу из списка
    app.group.delete_first_group()