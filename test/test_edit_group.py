__author__ = 'Natalia.Nikonova'
from model.group import group
import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(group(name="qwerty", header="asdf", footer="zxcv"))
    app.session.logout()