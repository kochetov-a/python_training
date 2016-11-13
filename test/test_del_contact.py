# -*- coding: utf-8 -*-

from model.contact import Contact

def test_delete_first_contact(app):
    # Если на странице нет контактов
    if app.contact.count_contact() == 0:
        # Создаём новый контакт для удаления
        app.contact.create(Contact(first_name="Contact for delete"))
    # Удаляем первый контакт из списка
    app.contact.delete_first_contact()