# класс для работы с сессией
class SessionHelper:

    def __init__(self, app):
        self.app = app

    # метод логина на сайт
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

    # метод логаута
    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    # удаляем фикстуру после завершения теста
    def destroy(self):
        self.app.wd.quit()

    # проверка того что произведён выход с сайта
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    # проверяем что произведён логин на сайт
    def is_logged_in(self):
        wd = self.app.wd
        # Если на странице есть элемент с текстом "Logout" считаем что произошел логаут
        return len(wd.find_elements_by_link_text("Logout")) > 0

    # проверяем что пользователь зашел на сайт под ожидаемым именем
    def is_logged_in_as(self, username):
        wd = self.app.wd
        # Если на странице есть элемент с текстом который соответсвует имени пользователя, то есть логин
        return wd.find_element_by_xpath("//div/div/[1]/form/b").text == "("+username+")"

    # проверяем что пользователь не вышел во время выполнения теста
    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
