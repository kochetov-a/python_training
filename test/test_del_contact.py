# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange

# Удаление случайного контакта из списка
def test_delete_some_contact(app):
    if app.contact.count_contact() == 0:  # Если на странице нет контактов
        app.contact.create(Contact(first_name="ContactTest"))  # Создаём новый контакт
    old_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ДО добавления
    index = randrange(len(old_contacts)) # Получение номера случайного контакта для удаления
    app.contact.delete_contact_by_index(index)  # Удаляем выбранный контакт из списка
    new_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ПОСЛЕ добавления
    assert len(old_contacts) - 1 == len(new_contacts)  # Проверка что на один контакт стало больше
    old_contacts[index:index + 1] = []  # Удаляем выбранный контакт из старого списка
    assert old_contacts == new_contacts # Сравнение что списки контактов равны