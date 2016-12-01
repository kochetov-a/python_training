# -*- coding: utf-8 -*-

import re
from random import randrange


# Тест сравнения данных контакта с главной страницы с данными из формы редактирования
def test_compare_data_from_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))  # Получаем значение для случайного выбора контакта
    data_from_home_page = app.contact.get_contact_list()[index]  # Получаем данные с главной страницы
    data_from_edit_page = app.contact.get_contact_info_from_edit_page(index)  # Получаем данные с формы редактирования
    # Сравниваем список телефонов с главной страницы со склеенной строкой из формы редактирования
    assert data_from_home_page.all_phones == merge_phones_like_on_home_page(data_from_edit_page)
    # Сравниваем список эл. адресов с главной страницы со склеенной строкой из формы редактирования
    assert data_from_home_page.all_emails == merge_emails_like_on_home_page(data_from_edit_page)
    assert data_from_home_page.first_name == data_from_edit_page.first_name  # Сравнение имени
    assert data_from_home_page.last_name == data_from_edit_page.last_name  # Сравнение фамилии
    assert data_from_home_page.address == data_from_edit_page.address  # Сравнение адреса


# Функция удаления ненужных символов перед сравнением
def clear(s):
    return re.sub("[() -]", "", s)


# Склеевание строки из элементов формы редактирования
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # Отфильтровываются пустые строки, то что осталось склеивается
                            map(lambda x: clear(x),  # Элементы очищаются от ненужных символов
                                    filter(lambda x: x is not None,  # Из списка фильтруются пустые элементы
                                        [contact.home_phone, contact.mobile_phone,
                                            contact.work_phone, contact.secondary_phone]))))


# Склеевание строки из элементов формы редактирования
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # Отфильтровываются пустые строки, то что осталось склеивается
                            map(lambda x: clear(x),  # Элементы очищаются от ненужных символов
                                filter(lambda x: x is not None,  # Из списка фильтруются пустые элементы
                                       [contact.email, contact.email_2, contact.email_3]))))