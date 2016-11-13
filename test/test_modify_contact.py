# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_contact_first_name(app):
    # Если на странице нет контактов
    if app.contact.count_contact() == 0:
        # Создаём новый контакт для модификации
        app.contact.create(Contact(first_name="Name for modify"))
    # Модифицируем первый контакт из списка
    app.contact.modify_first_contact(Contact(first_name="New name"))