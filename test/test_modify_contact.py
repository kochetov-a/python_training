# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_contact_first_name(app):
    if app.contact.count_contact() == 0: # Если на странице нет контактов
        app.contact.create(Contact(first_name="FirstTest", last_name="LastTest"))  # Создаём новый контакт для модификации
    contact = Contact(first_name="Petr", last_name="Petrov")  # Новые параметры для групп в переменную
    old_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ДО модификации
    contact.id = old_contacts[0].id  # Сохраняем id первого контакта
    app.contact.modify_first_contact(contact)  # Модифицируем первый контакт из списка
    new_contacts = app.contact.get_contact_list()  # Сохранение списка контактов ПОСЛЕ модификации
    assert len(old_contacts) == len(new_contacts)  # Проверяем что количество контактов не изменилось
    old_contacts[0] = contact  # Добавление новых параметров контакту по id
    # Сравниваем отсортированные по ключу (id) списки контактов
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)