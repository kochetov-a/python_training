# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()  # Сохранение списка контактов ДО добавления
    app.contact.create(contact)  # Создание нового контакта
    new_contacts = db.get_contact_list()  # Сохранение списка контактов ПОСЛЕ добавления
    old_contacts.append(contact)  # Добавляем параметры нового контакта в старый список
    # Сравниваем отсортированные по ключу (id) списки контактов
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

