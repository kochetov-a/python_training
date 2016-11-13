# -*- coding: utf-8 -*-

from model.group import Group

def test_delete_first_group(app):
    if app.group.count_group() == 0: # Если на странице групп, нет групп
        app.group.create(Group(name="Group for delete")) # Создаём новую группу для удаления
    app.group.delete_first_group() # Удаляем первую группу из списка