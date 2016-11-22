# -*- coding: utf-8 -*-

from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count_contact() == 0:  # Если на странице нет контактов
        app.contact.create(Contact(first_name="ContactTest"))  # Создаём новый контакт для удаления
    old_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ДО добавления
    app.contact.delete_first_contact()  # Удаляем первый контакт из списка
    new_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ПОСЛЕ добавления
    assert len(old_contacts) - 1 == len(new_contacts)  # Проверка что на один контакт стало больше
    old_contacts[0:1] = []  # Удаляем первый контакт из старого списка
    assert old_contacts == new_contacts # Сравнение что списки контактов равны