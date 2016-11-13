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

    # Функция заполнения формы создания нового контакта
    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.second_name)
        self.change_field_value("lastname", contact.last_name)

    # Функция изменения полей контакта
    def change_field_value(self, field_name, text):
        wd = self.app.wd
        # Если переменная "text" не пустая,то передаём её значение в поля
        if text is not None:
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

    # Функция модификации первого контакта из списка
    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # click edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # submit_new_contact
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    # Подсчет количества контактов на странице
    def count_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        # Функция возвращает количество найденных на странице элементов
        return len(wd.find_elements_by_name("selected[]"))