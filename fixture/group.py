# Класс-помощник для работы с группами
class GroupHelper:

    def __init__(self, app):
        self.app = app

    # Открытие страницы с группами (http://localhost/addressbook/group.php)
    def open_group_page(self):
        wd = self.app.wd
        # Если открыта НЕ страница с группами, то перейти на неё (проверка по URL и наличию кнопки)
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    # Функция открытия формы для создания новой группы
    def create_new_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    # Функция создания новой группы
    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.create_new_group()
        self.fill_group_form(group)
        # submit_group_creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    # Функция выбора первой группы из списка
    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    # Функция возврата на страницу с группами
    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    # Функция заполнения формы создания группы
    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_filed_value("group_name", group.name)
        self.change_filed_value("group_header", group.header)
        self.change_filed_value("group_footer", group.footer)

    # Изменение содержимого полей групп (передаём: имя поля, содержимое)
    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        # Если содержимое поля (text) не пустое, то передаём его в поле (field_name)
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    # Удаление первой группы из списка
    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click() # Удаляем первую группу из списка
        self.return_to_group_page()

    # Модификация первой группы из списка
    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # Открываем форму для редактирования
        wd.find_element_by_name("edit").click()
        # Заполняем форму новым содержимым (переменная "new_group_data")
        self.fill_group_form(new_group_data)
        # Подтверждаем изменения
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    # Подсчет количества групп на странице
    def count_group(self):
        wd = self.app.wd
        self.open_group_page()
        # Функция возвращает количество найденных на странице элементов
        return len(wd.find_elements_by_name("selected[]"))