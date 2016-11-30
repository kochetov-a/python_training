# -*- coding: utf-8 -*-

from model.contact import Contact
import re

# Класс-помощник для работы с контактами
class ContactHelper:

    def __init__(self, app):
        self.app = app

    # Функция создания нового контакта
    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit_new_contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    # Функция заполнения формы создания нового контакта
    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.second_name)
        self.change_field_value("lastname", contact.last_name)

    # Функция изменения полей контакта
    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None: # Если переменная "text" не пустая,то передаём её значение в поля
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    # Функция возвращения на главную страницу
    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    # Функция удаления первого контакта из списка (не используется)
    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    # Функция удаления случайного контакта из списка
    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    # Функция модификации первого контакта из списка (не используется)
    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    # Подсчет количества контактов на странице
    def count_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        # Функция возвращает количество найденных на странице элементов
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None  # Переменная для кеша списка контактов

    # Получение списка контактов на странице
    def get_contact_list(self):
        if self.contact_cache is None:  # Если кеш списка контактов пуст, то заполняем его
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []  # Создание пустого списка "contacts"
            for row in wd.find_elements_by_name("entry"):  # Получение списка строк на странице
                cells = row.find_elements_by_tag_name("td")  # Получение содержимого ячеек из строк
                id = row.find_element_by_name("selected[]").get_attribute("value")  # id из первой ячейки
                first_name = cells[2].text  # Имя из третьей ячейки
                last_name = cells[1].text  # Фамилию из второй ячейки
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name,
                                                  home_phone=all_phones[0], mobile_phone=all_phones[1],
                                                  work_phone=all_phones[2], secondary_phone=all_phones[3]))
        return list(self.contact_cache)  # Возвращаем список контактов


    # Функция модификации случайного контакта из списка (по индексу)
    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()  # Отмечаем чек-бокс выбранного контакта
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()  # Нажимаем "Edit"
        self.fill_contact_form(new_contact_data)  # Изменяем данные контакта
        wd.find_element_by_name("update").click()  # Нажимаем кнопку "Update" для применение изменений
        self.return_to_home_page()
        self.contact_cache = None

    # Функция просмотра детальной информации контакта из списка по индексу
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[7]/a/img")[index].click()  # Нажимаем "Details"

    # Функция чтения информации из формы редактирования
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()  # Нажимаем "Edit"

    # Функция получения номеров телефона из страницы редактирования
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)   # Открываем страницу редактирования контактов
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        self.return_to_home_page()
        return Contact(first_name=first_name, last_name=last_name, id=id,
                       home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)

    # Функция получения номеров телефона из страницы просмотра детальной информации
    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)  # Открываем страницу просмотра информации
        text = wd.find_element_by_id("content").text  # Находим блок с телефонами
        home_phone = re.search("H: (.*)", text).group(1)  # Получаем домашний телефон
        work_phone = re.search("W: (.*)", text).group(1)  # Получаем рабочий телефон
        mobile_phone = re.search("M: (.*)", text).group(1)   # Получаем мобильный телефон
        secondary_phone = re.search("P: (.*)", text).group(1)   # Получаем дополнительный телефон
        self.return_to_home_page()   # Возвращаемся на главную страницу
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone)