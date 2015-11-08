__author__ = 'Natalia.Nikonova'
from model.group import group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(group(name="bbb", header="ccc", footer="ddd"))
    app.group.delete_first_group()
