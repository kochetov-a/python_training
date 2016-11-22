# -*- coding: utf-8 -*-

from model.contact import Contact

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

    # Функция удаления первого контакта из списка
    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    # Функция модификации первого контакта из списка
    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()  # select first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()  # click edit
        self.fill_contact_form(new_contact_data)  # submit_new_contact
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    # Подсчет количества контактов на странице
    def count_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        # Функция возвращает количество найденных на странице элементов
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None  # Переменная для кеша списка контактов

    # Получение списка контактов на странице
    def get_contact_list(self):
        if self.contact_cache is None: # Если кеш списка контактов пуст, то заполняем его
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []  # Создание пустого списка "contacts"
            for row in wd.find_elements_by_name("entry"):  # Получение списка строк на странице
                cells = row.find_elements_by_tag_name("td")  # Получение содержимого ячеек из строк
                id = row.find_element_by_name("selected[]").get_attribute("value") # id из первой ячейки
                f_name = cells[2].text # Имя из третьей ячейки
                l_name = cells[1].text # Фамилию из второй ячейки
                # Заполнение списка групп полученными значениями
                self.contact_cache.append(Contact(id=id, first_name=f_name, last_name=l_name))
        return list(self.contact_cache)  # Возвращаем список контактов
