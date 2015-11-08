__author__ = 'Natalia.Nikonova'

from model.group import group

def test_edit_first_group_data(app):
    if app.group.count() == 0:
        app.group.create(group(name="bbb", header="ccc", footer="ddd"))
    app.group.edit_first_group(group(name="qwerty", header="asdf", footer="zxcv"))


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(group(name="bbb", header="ccc", footer="ddd"))
    app.group.edit_first_group_data(group(name="New group"))
