from model.group import Group


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
        self.group_cache = None

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
        self.delete_group_by_index(0)

    # Функция выбора группы по index
    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    # Удаление случайной группы из списка
    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)  # Выбираем группу из списка по индексу
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0)

    # Модификация группы по index
    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # Открываем форму для редактирования
        wd.find_element_by_name("edit").click()
        self.app.wd.implicitly_wait(20)
        # Заполняем форму новым содержимым (переменная "new_group_data")
        self.fill_group_form(new_group_data)
        # Подтверждаем изменения
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    # Подсчет количества групп на странице
    def count_group(self):
        wd = self.app.wd
        self.open_group_page()
        # Функция возвращает количество найденных на странице элементов
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None  # Переменная для кеша списка групп

    # Получение списка групп на странице
    def get_group_list(self):
        if self.group_cache is None:  # Если кеш списка групп пуст, то заполняем его
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []  # Создание пустого списка "groups"
            for element in wd.find_elements_by_css_selector("span.group"):  # Получение списка групп на странице
                text = element.text  # Получение названия группы
                id = element.find_element_by_name("selected[]").get_attribute("value")  # Получение id группы
                # Заполнение списка групп полученными значениями
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)  # Возвращаем список групп

    # Выбор группы по id из базы данных для удаления
    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)  # Выбираем группу из списка по индексу
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    # Модификация группы по id
    def modify_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)  # Выбираем группу из списка по индексу
        wd.find_element_by_name("edit").click()
        # Заполняем форму новым содержимым (переменная "new_group_data")
        self.fill_group_form(new_group_data)
        # Подтверждаем изменения
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    # Выбор группы по id из базы данных
    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()