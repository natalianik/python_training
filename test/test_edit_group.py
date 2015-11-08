__author__ = 'Natalia.Nikonova'

from model.group import group

def test_edit_first_group_data(app):
    app.group.edit_first_group(group(name="qwerty", header="asdf", footer="zxcv"))


def test_edit_first_group_name(app):
    app.group.edit_first_group_data(group(name="New group"))
