# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact

def test_add_first_contact_to_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.add_first_contact_to_first_group()
