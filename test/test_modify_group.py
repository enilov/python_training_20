# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="group1", header="group1", footer="group1"))
    app.session.logout()


