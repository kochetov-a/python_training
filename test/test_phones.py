# -*- coding: utf-8 -*-

import re

# Тест сравнения телефонов контакта из формы редактирования и главной страницы
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

# Тест сравнения телефонов контакта из формы редактирования и формы просмотра детальной информации
def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone

# Функция удаления ненужных символов для сравнения
def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",  # Отфильтровываются пустые строки, то что осталось склеивается
                            map(lambda x: clear(x),  # Элементы очищаются от ненужных символов
                                    filter(lambda x: x is not None,  # Из списка фильтруются пустые элементы
                                        [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))