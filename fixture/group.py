# class for work with group
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create_new_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.create_new_group()
        self.fill_group_form(group)
        # submit_group_creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_filed_value("group_name", group.name)
        self.change_filed_value("group_header", group.header)
        self.change_filed_value("group_footer", group.footer)

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # delete first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open edit form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit change group name
        wd.find_element_by_name("update").click()
        self.return_to_group_page()