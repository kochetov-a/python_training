# -*- coding: utf-8 -*-

from model.contact import Contact

def test_modify_contact_first_name(app):
    app.contact.modify_first_contact(Contact(first_name="New name"))

def test_modify_contact_second_name(app):
    app.contact.modify_first_contact(Contact(second_name="New second name"))