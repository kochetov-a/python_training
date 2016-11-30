# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ДО добавления
    contact = Contact(first_name="Ivan", last_name="Ivanov")  # Параметры контакта в переменную
    app.contact.create(contact)  # Создание нового контакта
    assert len(old_contacts) + 1 == app.contact.count_contact()  # Проверка что на один контакт стало больше
    new_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ПОСЛЕ добавления
    old_contacts.append(contact)  # Добавляем параметры нового контакта в старый список
    # Сравниваем отсортированные по ключу (id) списки контактов
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ДО добавления
#     contact = Contact(first_name="", last_name="")  # Параметры контакта в переменную
#     app.contact.create(contact)  # Создание нового контакта
#     new_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ПОСЛЕ добавления
#     assert len(old_contacts) + 1 == len(new_contacts)  # Проверка что на один контакт стало больше
#     old_contacts.append(contact)  # Добавляем параметры нового контакта в старый список
#     # Сравниваем отсортированные по ключу (id) списки контактов
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)