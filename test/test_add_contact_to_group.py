from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# Тест проверки добавления контакта в группу (контакт не входит в эту группу)
def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:  # Если в базе данных нет групп, то создаём новую группу
        app.group.create(Group(name="TestNameForGroup", header="TestHeaderForGroup", footer="TestFooterForGroup"))
    if len(db.get_contact_list()) == 0:  # Если в базе данных нет контактов, то создаём новый контакт
        app.contact.create(Contact(first_name="first_name_test", last_name="last_name_test"))
    group = random.choice(db.get_group_list())  # Выбираем случайную группу из списка групп
    if len(orm.get_contacts_not_in_group(Group(id=group.id))) == 0:  # Если нет контактов которые не входят в эту группу
        app.contact.create(Contact(first_name="first_name_test_88", last_name="last_name_test_89"))  # Создаём новый
    # Выбираем контакт который НЕ ВХОДИТ в выбранную группу
    contact = random.choice(orm.get_contacts_not_in_group(Group(id=group.id)))
    old_groups = orm.get_contacts_in_group(Group(id=group.id))   # Получаем состав группы ДО добавления
    app.contact.add_to_group(contact.id, group.id)  # Добавляем случайный контакт в случайную группу
    new_groups = orm.get_contacts_in_group(Group(id=group.id))  # Получаем состав группы ПОСЛЕ добавления
    if contact not in old_groups:   # Если этого контакта еще нет в старом списке
        old_groups.append(contact)  # То добавляем его, если есть – то НЕ добавляем
    # Сравниваем содержание выбранной группы ДО и ПОСЛЕ добавления
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# Тест проверки добавления контакта в группу (контакт входит в эту группу)
def test_add_contact_to_group_again(app, db):
    if len(db.get_group_list()) == 0:  # Если в базе данных нет групп, то создаём новую группу
        app.group.create(Group(name="TestNameForGroup", header="TestHeaderForGroup", footer="TestFooterForGroup"))
    if len(db.get_contact_list()) == 0:  # Если в базе данных нет контактов, то создаём новый контакт
        app.contact.create(Contact(first_name="first_name_test", last_name="last_name_test"))
    group = random.choice(db.get_group_list())  # Выбираем случайную группу из списка групп
    if len(orm.get_contacts_in_group(Group(id=group.id))) == 0:  # Если в этой группе нет контактов
        contact = random.choice(db.get_contact_list())  # Выбираем случайный из списка
        app.contact.add_to_group(contact.id, group.id)  # Добавляем его в эту группу
    contact = random.choice(orm.get_contacts_in_group(Group(id=group.id)))  # Выбираем случайный контакт из группы
    old_groups = orm.get_contacts_in_group(Group(id=group.id))   # Получаем состав группы ДО добавления
    app.contact.add_to_group(contact.id, group.id)  # Добавляем контакт в группу
    new_groups = orm.get_contacts_in_group(Group(id=group.id))  # Получаем состав группы ПОСЛЕ добавления
    # Сравниваем содержание выбранной группы ДО и ПОСЛЕ добавления
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)