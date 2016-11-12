# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_contact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="New name"))
    app.session.logout()

def test_modify_contact_second_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(second_name="New second name"))
    app.session.logout()