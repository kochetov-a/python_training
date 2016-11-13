# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application

fixture = None

# Фикстура логина на сайт с проверкой валидности фикстуры
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        # Если фикстура не валидна
        if not fixture.is_valid():
            # Инициализируем фикстуру
            fixture = Application()
    # Открываем главную страницу в любом случае
    fixture.open_home_page()
    # Выполняем логин в любом случае
    fixture.session.ensure_login(username="admin", password="secret")
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