# -*- coding: utf-8 -*-

import re
from random import randrange

# Тест сравнения телефонов контакта на главной странице с данными из формы редактирования
def test_phones_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]  # Получаем телефоны с главной страницы
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)  # Получаем телефоны с формы редактирования
    # Сравниваем список телефонов с главной страницы со склеенной строкой из формы редактирования
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

# Тест сравнения имени, фамилии, адреса на главной странице с данными из формы редактирования
def test_name_lastname_address_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    data_from_home_page = app.contact.get_contact_list()[index]  # Получаем данные с главной страницы
    data_from_edit_page = app.contact.get_contact_info_from_edit_page(index)  # Получаем данные с формы редактирования
    assert data_from_home_page.first_name == data_from_edit_page.first_name  # Сравнение имени
    assert data_from_home_page.last_name == data_from_edit_page.last_name  # Сравнение фамилии
    assert data_from_home_page.address == data_from_edit_page.address  # Сравнение адреса

# Тест сравнения электронных адресов контакта на главной странице с данными из формы редактирования
def test_emails_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    emails_from_home_page = app.contact.get_contact_list()[index]  # Получаем эл. почту с главной страницы
    emails_from_edit_page = app.contact.get_contact_info_from_edit_page(index)  # Получаем эл. почту с формы редактирования
    # Сравниваем список эл. адресов с главной страницы со склеенной строкой с формы редактирования
    assert emails_from_home_page.all_emails == merge_emails_like_on_home_page(emails_from_edit_page)

# Функция удаления ненужных символов перед сравнением
def clear(s):
    return re.sub("[() -]", "", s)

# Склеевание строки из элементов формы редактирования
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # Отфильтровываются пустые строки, то что осталось склеивается
                            map(lambda x: clear(x),  # Элементы очищаются от ненужных символов
                                    filter(lambda x: x is not None,  # Из списка фильтруются пустые элементы
                                        [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))

# Склеевание строки из элементов формы редактирования
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # Отфильтровываются пустые строки, то что осталось склеивается
                            map(lambda x: clear(x),  # Элементы очищаются от ненужных символов
                                filter(lambda x: x is not None,  # Из списка фильтруются пустые элементы
                                       [contact.email, contact.email_2, contact.email_3]))))

# # Тест сравнения телефонов контакта из формы редактирования и формы просмотра детальной информации
# def test_phones_on_contact_view_page(app):
#     contacts = app.contact.get_contact_list()
#     index = randrange(len(contacts))
#     contact_from_view_page = app.contact.get_contact_from_view_page(index)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
#     assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
#     assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
#     assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone