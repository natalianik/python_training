# -*- coding: utf-8 -*-
import pytest
from group import group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(group(name="bbb", header="ccc", footer="ddd"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(group(name="", header="", footer=""))
    app.logout()
