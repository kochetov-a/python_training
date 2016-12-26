# -*- coding: utf-8 -*-

import re
from model.contact import Contact


# Тест сравнения данных контакта с главной страницы с данными из базы данных
def test_compare_data_from_home_page(app, db):
    data_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)  # Данные с главной страницы
    data_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)  # Данные из БД
    # Цикл для сравнения отдельных полей списков
    for i in range(len(data_from_db)):
        assert data_from_home_page[i].first_name == data_from_db[i].first_name  # Сравниваем имя
        assert data_from_home_page[i].last_name == data_from_db[i].last_name  # Сравниваем фамилию
        assert data_from_home_page[i].address == data_from_db[i].address  # Сравниваем адрес
        # Сравниваем список эл. адресов с главной страницы со склеенной строкой из БД
        assert data_from_home_page[i].all_emails == merge_emails_like_on_home_page(data_from_db[i])
        # Сравниваем список телефонов с главной страницы со склеенной строкой из БД
        assert data_from_home_page[i].all_phones == merge_phones_like_on_home_page(data_from_db[i])


# Функция удаления ненужных символов перед сравнением телефонов
def clear_phones(s):
    return re.sub("[() -]", "", s)

# Функция удаления ненужных символов перед сравнением эл. адресов
def clear_mails(s):
    return re.sub(" ", "", s)


# Склеевание строки из элементов БД (телефоны)
def merge_phones_like_on_home_page(db):
    return "\n".join(filter(lambda x: x != "",  # Отфильтровываются пустые строки, то что осталось склеивается
                            map(lambda x: clear_phones(x),  # Элементы очищаются от ненужных символов
                                    filter(lambda x: x is not None,  # Из списка фильтруются пустые элементы
                                        [db.home_phone, db.mobile_phone,
                                            db.work_phone, db.secondary_phone]))))


# Склеевание строки из элементов БД (эл. адреса)
def merge_emails_like_on_home_page(db):
    return "\n".join(filter(lambda x: x != "",  # Отфильтровываются пустые строки, то что осталось склеивается
                            map(lambda x: clear_mails(x),  # Элементы очищаются от ненужных символов
                                filter(lambda x: x is not None,  # Из списка фильтруются пустые элементы
                                       [db.email, db.email_2, db.email_3]))))