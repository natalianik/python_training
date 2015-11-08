# -*- coding: utf-8 -*-

from model.group import group

def test_add_group(app):
    app.group.create(group(name="bbb", header="ccc", footer="ddd"))


def test_add_empty_group(app):
    app.group.create(group(name="", header="", footer=""))
