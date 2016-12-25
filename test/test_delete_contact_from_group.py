from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# Тест проверки удаления случайного контакта из случайной группы
def test_delete_contact_from_group(app, db):
    group = random.choice(db.get_group_list())  # Выбор случайной группы
    if len(orm.get_contacts_in_group(Group(id=group.id))) == 0:  # Если в группе нет контактов
        contact = random.choice(db.get_contact_list())  # Выбираем случайный контакт из списка
        app.contact.add_to_group(contact.id, group.id)  # и добавляем его в группу
    old_groups = orm.get_contacts_in_group(Group(id=group.id))  # Получаем состав группы ДО удаления
    contact = random.choice(old_groups)     # Выбираем контакт из группы для удаления
    app.contact.delete_from_group(contact.id, group.id)  # Удаляем выбранный контакт из группы
    new_groups = orm.get_contacts_in_group(Group(id=group.id))  # Получаем состав группы ПОСЛЕ удаления
    old_groups.remove(contact)  # Удаляем контакт из старого списка
    # Сравниваем содержание выбранной группы ДО и ПОСЛЕ удаления контакта
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)