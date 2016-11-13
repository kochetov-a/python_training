# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_contact_first_name(app):
    if app.contact.count_contact() == 0: # Если на странице нет контактов
        app.contact.create(Contact(first_name="Name for modify")) # Создаём новый контакт для модификации
    app.contact.modify_first_contact(Contact(first_name="New name")) # Модифицируем первый контакт из списка