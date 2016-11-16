# Класс-помощник для работы с сессией
class SessionHelper:

    def __init__(self, app):
        self.app = app

    # Функция входа на сайт
    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    # Функция выхода с сайта
    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    # Функция удаления фикстуры после завершения теста
    def destroy(self):
        self.app.wd.quit()

    # Функция проверки выхода с сайта
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    # Функция проверки входа на сайт
    def is_logged_in(self):
        wd = self.app.wd
        # Если на странице есть элемент с текстом "Logout", то пользователь вошел на сайт
        return len(wd.find_elements_by_link_text("Logout")) > 0

    # Функция проверки имени с которым произошел вход на сайт
    def is_logged_in_as(self, username):
        wd = self.app.wd
        # Если на странице есть элемент с текстом который соответсвует имени пользователя, то есть логин
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

    # Функция проверки логина во время прогона тестов
    def ensure_login(self, username, password):
        wd = self.app.wd
        # Если пользователь вошел на сайт
        if self.is_logged_in():
            # И если пользователь вошел на сайт под ожидаемым именем
            if self.is_logged_in_as(username):
                # Тогда ничего не делаем
                return
            else:
                # Иначе производим выход с сайта, для последующего входа
                self.logout()
        self.login(username, password)