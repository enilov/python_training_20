# -*- coding: utf-8 -*-
from model.contact import Contact


def test_view_and_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    test_contact = Contact(first_name="MODIFIED VIA VIEW")
    app.contact.view_details_and_modify_first(test_contact)

