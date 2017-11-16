# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="name", middle_name="mid_name", last_name="last_name",
                           nick_name="nick_name", title="title", company="company", address="address",
                           home_phone="123", mobile_phone="321", work_phone="456", fax_phone="654",
                           email="1@mail.ru")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="", middle_name="", last_name="",
                           nick_name="", title="", company="", address="",
                           home_phone="", mobile_phone="", work_phone="", fax_phone="",
                           email="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

