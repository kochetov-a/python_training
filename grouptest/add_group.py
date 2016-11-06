# -*- coding: utf-8 -*-

import pytest

from groupfixture.application import Application
from groupmodel.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.fill_group_form(Group(name="Test1", header="test_header", footer="test_footer"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.fill_group_form(Group(name="", header="", footer=""))
    app.session.logout()