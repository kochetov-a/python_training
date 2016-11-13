# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application

@pytest.fixture (scope = "session")
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.session.destroy()
    request.addfinalizer(fin)
    return fixture