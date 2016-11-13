# -*- coding: utf-8 -*-

from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count_contact() == 0: # Если на странице нет контактов
        app.contact.create(Contact(first_name="Contact for delete")) # Создаём новый контакт для удаления
    app.contact.delete_first_contact() # Удаляем первый контакт из списка