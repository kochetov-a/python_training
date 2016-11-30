# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application

fixture = None

# Фикстура логина на сайт с проверкой валидности фикстуры
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        # Если фикстура не валидна
        if not fixture.is_valid():
            # Инициализируем фикстуру
            fixture = Application(browser=browser, base_url=base_url)
    # Открываем главную страницу в любом случае
    fixture.open_home_page()
    # Выполняем логин в любом случае
    fixture.session.ensure_login(username=login, password=password)
    return fixture

# Фикстура выхода из приложения
@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        # Убеждаемся что пользователь вылогинился
        fixture.session.ensure_logout()
        # Разрушаем фикстуру
        fixture.session.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--login", action="store", default="Admin")
    parser.addoption("--password", action="store", default="secret")
