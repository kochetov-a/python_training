from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# Тест проверки добавления случайного контакта в случайную группу
def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:  # Если в базе данных нет групп, создаем группу
        app.group.create(Group(name="TestNameForGroup", header="TestHeaderForGroup",
                               footer="TestFooterForGroup"))    # Создаём новую группу
    group = random.choice(db.get_group_list())      # Выбор случайной группы
    contact = random.choice(db.get_contact_list())  # Выбор случайного контакта
    old_groups = orm.get_contacts_in_group(Group(id=group.id))   # Получаем состав группы ДО добавления
    app.contact.add_to_group(contact.id, group.id)  # Добавляем случайный контакт в случайную группу
    new_groups = orm.get_contacts_in_group(Group(id=group.id))  # Получаем состав группы ПОСЛЕ добавления
    if contact not in old_groups:   # Если этого контакта еще нет в старом списке
        old_groups.append(contact)  # То добавляем его, если есть – то НЕ добавляем
    # Сравниваем содержание выбранной группы ДО и ПОСЛЕ добавления
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)