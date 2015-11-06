__author__ = 'Natalia.Nikonova'
from model.group import group

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(group(name="qwerty", header="asdf", footer="zxcv"))
    app.session.logout()