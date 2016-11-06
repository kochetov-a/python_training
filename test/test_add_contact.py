# -*- coding: utf-8 -*-

import pytest

from fixture.application_contact import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Ivan", second_name="Ivanovich", last_name="Ivanov"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", second_name="", last_name=""))
    app.session.logout()