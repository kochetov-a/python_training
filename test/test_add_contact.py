# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()  # Получение списка контактов из БД до добавления
    app.contact.create(contact)  # Создание нового контакта
    new_contacts = db.get_contact_list()  # Получение списка контактов из БД после добавления
    old_contacts.append(contact)  # Добавляем параметры нового контакта в старый список
    # Сравниваем отсортированные по ключу (id) списки контактов
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:  # Включение проверки графического интерфейса при наличии ключа "--check_ui"
        # Сравниваем отсортированные по ключу (id) списки контактов
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

