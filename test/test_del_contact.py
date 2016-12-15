# -*- coding: utf-8 -*-

from model.contact import Contact
import random


# Удаление случайного контакта из списка
def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:  # Если на странице нет контактов
        app.contact.create(Contact(first_name="ContactTest"))  # Создаём новый контакт
    old_contacts = db.get_contact_list()  # Сохранение списка контактов ДО добавления
    contact = random.choice(old_contacts)  # Получение номера случайного контакта для удаления
    app.contact.delete_contact_by_id(contact.id)  # Удаляем выбранный контакт из списка
    new_contacts = db.get_contact_list()  # Сохранение списка контактов ПОСЛЕ добавления
    old_contacts.remove(contact)  # Удаляем выбранный контакт из старого списка
    assert old_contacts == new_contacts  # Сравнение что списки контактов равны