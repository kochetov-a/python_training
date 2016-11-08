# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="first_name_1", second_name="second_name_1", last_name="last_name_1", company_name="Yandex"))
    app.session.logout()