# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="user_first_name", second_name="user_seconf_name", last_name="user_last_name", company_name=""))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", second_name="", last_name="", company_name="Yandex"))
    app.session.logout()