# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(first_name="user_first_name", second_name="user_seconf_name", last_name="user_last_name", company_name=""))

def test_add_empty_contact(app):
    app.contact.create(Contact(first_name="", second_name="", last_name="", company_name="Yandex"))
