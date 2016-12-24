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
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    # Функция заполнения формы создания нового контакта
    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.second_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("company", contact.company_name)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)

    # Функция изменения полей контакта
    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:  # Если переменная "text" не пустая,то передаём её значение в поля
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

    # Функция удаления контакта из списка по индексу
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
        return len(wd.find_elements_by_name("selected[]"))  # Возвращает количество найденных на странице элементов

    # Переменная для кеша списка контактов
    contact_cache = None

    # Получение списка контактов на главной странице
    def get_contact_list(self):
        if self.contact_cache is None:  # Если кеш списка контактов пуст, то заполняем его
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []  # Создание пустого списка "contacts"
            for row in wd.find_elements_by_name("entry"):  # Получение списка строк на странице
                cells = row.find_elements_by_tag_name("td")  # Получение содержимого ячеек из строк
                id = row.find_element_by_name("selected[]").get_attribute("value")  # id из первой ячейки
                last_name = cells[1].text  # Фамилию из из ячейки №1
                first_name = cells[2].text  # Имя из из ячейки №2
                address = cells[3].text  # Адрес из из ячейки №3
                all_emails = cells[4].text  # Все e-mail'ы из ячейки №4
                all_phones = cells[5].text  # Все телефоны из ячейки №5
                self.contact_cache.append(Contact(id=id, first_name=first_name, last_name=last_name,
                                                  address=address, all_phones=all_phones,
                                                  all_emails=all_emails))
        return list(self.contact_cache)  # Возвращаем список контактов

    # Функция модификации контакта из списка по индексу
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
        wd.find_elements_by_name("selected[]")[index].click()  # Отмечаем чек-бокс выбранного контакта
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[7]/a/img")[index].click()  # Нажимаем "Details"

    # Функция просмотра формы редактирования контакта из списка по индексу
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()  # Отмечаем чек-бокс выбранного контакта
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()  # Нажимаем "Edit"

    # Функция получения различных данных из формы редактирования контакта
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)   # Открываем страницу редактирования контактов
        id = wd.find_element_by_name("id").get_attribute("value")
        first_name = wd.find_element_by_name("firstname").get_attribute("value")  # Имя из поля "firstname"
        last_name = wd.find_element_by_name("lastname").get_attribute("value")  # Фамилию из поля "lastname""
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        self.return_to_home_page()
        return Contact(first_name=first_name, last_name=last_name, id=id,
                       home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, secondary_phone=secondary_phone,
                       address=address, email=email, email_2=email_2, email_3=email_3)

    # Функция удаления контакта по id
    def delete_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    # Функция модификации контакта по id
    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()  # Открываем форму редактирования по id
        self.fill_contact_form(new_contact_data)  # Изменяем данные контакта
        wd.find_element_by_name("update").click()  # Нажимаем кнопку "Update" для применение изменений
        self.return_to_home_page()  # Возвращаемся на главную страницу
        self.contact_cache = None

    # Функция добавления контакта в группу
    def add_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.return_to_home_page()  # Возвращаемся на главную страницу
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()   # Выбираем контакт
        wd.find_element_by_xpath("//select[@name='to_group']//option[@value='%s']" % group_id).click()  # Выбираем группу
        wd.find_element_by_name("add").click()  # Добавляем контакт в выбранную группу
        self.return_to_home_page()  # Возвращаемся на главную страницу
        self.contact_cache = None