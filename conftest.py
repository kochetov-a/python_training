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
        if not fixture.is_valid(): # Если фикстура не валидна
            fixture = Application() # Инициализируем фикстуру
    fixture.open_home_page()
    fixture.session.ensure_login(username="admin", password="secret") # Выполняем логин в любом случае
    return fixture

# Фикстура выхода из приложения
@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout() # Убеждаемся что пользователь вылогинился
        fixture.session.destroy() # Разрушаем фикстуру
    request.addfinalizer(fin)
    return fixture