# -*- coding: utf-8 -*-

import pytest

from contactfixture.application_c import Application_c
from contactmodel.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application_c()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(first_name="Ivan", second_name="Ivanovich", last_name="Ivanov"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(first_name="", second_name="", last_name=""))
    app.logout()