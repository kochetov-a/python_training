# -*- coding: utf-8 -*-

from model.contact import Contact
import random


# Удаление случайного контакта из списка
def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:  # Получаем из БД список контактов
        app.contact.create(Contact(first_name="Contact Test"))  # Если список пустой,создаём новый контакт
    old_contacts = db.get_contact_list()  # Сохранение списка контактов из БД до добавления
    contact = random.choice(old_contacts)  # Получение номера случайного контакта для удаления
    app.contact.delete_contact_by_id(contact.id)  # Удаляем контакт по id
    new_contacts = db.get_contact_list()  # Сохранение списка контактов из БД после добавления
    old_contacts.remove(contact)  # Удаляем выбранный контакт из старого списка
    assert old_contacts == new_contacts  # Сравнение что списки контактов равны
    if check_ui:  # Включение проверки графического интерфейса при наличии ключа "--check_ui"
        # Сравниваем отсортированные по ключу (id) списки контактов
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)