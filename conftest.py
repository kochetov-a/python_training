# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None

# Фикстура логина на сайт с проверкой валидности фикстуры
@pytest.fixture
def app(request):
    global fixture  # Объявление глобальной переменной для фикстуры
    global target  # Объявление глобальной переменной для файла конфигурации
    if target is None:
        # Получаем месторасположение конфига из переменной __file__ и объеденяем его с "target.json"
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:  # Пробуем открыть файл конфигурации и присвоить его переменной "f"
            target = json.load(f)  # Загружаем в переменную "target" содержимое файла
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=target["browser"], base_url=target["baseUrl"])
    # Открываем главную страницу в любом случае
    fixture.open_home_page()
    # Выполняем логин в любом случае
    fixture.session.ensure_login(username=target["username"], password=target["password"])
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
    parser.addoption("--target", action="store", default="target.json")
