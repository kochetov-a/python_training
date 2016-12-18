# -*- coding: utf-8 -*-

from model.contact import Contact
from random import *


# Модификация случайного контакта из списка
def test_modify_contact_by_index(app, db, check_ui):
    if len(db.get_contact_list()) == 0:  # Получаем из БД список контактов
        app.contact.create(Contact(first_name="Contact Test", last_name="Test Contact"))  # Если список пустой,создаём новый контакт
    contact = Contact(first_name="first_name_test", last_name="last_name_test")  # Новые параметры для контакта
    old_contacts = db.get_contact_list()  # Сохранение списка контактов из БД до модификации
    index = randrange(len(old_contacts))  # Получение номера случайного контакта
    contact.id = old_contacts[index].id  # Сохраняем id первого контакта
    app.contact.modify_contact_by_id(contact.id, contact)  # Модифицируем выбранный контакт из списка
    new_contacts = db.get_contact_list()  # Сохранение списка контактов ПОСЛЕ модификации
    old_contacts[index] = contact  # Добавление новых параметров контакту по id
    # Сравниваем отсортированные по ключу (id) списки контактов
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:  # Включение проверки графического интерфейса при наличии ключа "--check_ui"
        # Сравниваем отсортированные по ключу (id) списки контактов
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)