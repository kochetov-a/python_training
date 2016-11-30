# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

# Генератор тестовых данных
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# Генерация тестовых данных
data_for_contact = [Contact(first_name="", last_name="")] + [
    Contact(first_name=random_string("first_name", 20), last_name=random_string("last_name", 20))
    for i in range(5)
]

@pytest.mark.parametrize("contact", data_for_contact, ids=[repr(x) for x in data_for_contact])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ДО добавления
    app.contact.create(contact)  # Создание нового контакта
    assert len(old_contacts) + 1 == app.contact.count_contact()  # Проверка что на один контакт стало больше
    new_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ПОСЛЕ добавления
    old_contacts.append(contact)  # Добавляем параметры нового контакта в старый список
    # Сравниваем отсортированные по ключу (id) списки контактов
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

