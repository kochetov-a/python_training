from model.group import Group
from timeit import timeit



# Тест сравнения списка групп полученного из UI и из базы данных
def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))  # Вывод на консоль время выполнения
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)