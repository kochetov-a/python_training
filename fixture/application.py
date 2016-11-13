from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    # запуск браузера
    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    # проверка валидности фикстуры
    def is_valid(self):
        try:
            self.wd.current_url # Если браузер может вернуть адрес страницы
            return True # То фикстура валидна
        except:
            return False

    # открытие главной страницы
    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    # разрушение фикстуры
    def destroy(self):
        self.wd.quit()