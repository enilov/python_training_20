# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    new_contact_data = Contact(first_name="EDITED")
    app.contact.edit_first_contact(new_contact_data)

