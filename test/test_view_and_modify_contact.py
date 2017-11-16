# -*- coding: utf-8 -*-
from model.contact import Contact


def test_view_and_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="MODIFIED")
    contact.id = old_contacts[0].id
    new_contacts = app.contact.get_contact_list()
    app.contact.view_details_and_modify_first(contact)
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

