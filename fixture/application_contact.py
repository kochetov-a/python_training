from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

class Application:

    # start the browser
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    # function
    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    # delete fixture
    def destroy(self):
        self.wd.quit()