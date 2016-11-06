from selenium.webdriver.firefox.webdriver import WebDriver
from contactfixture.session import SessionHelper
from contactfixture.contact import ContactHelper

class Application_c:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()