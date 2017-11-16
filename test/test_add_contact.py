# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="name", middlename="mid_name", lastname="last_name",
                      address="address",homephone="123456789", mobilephone="9876543210", workphone="1111111",
                      secondaryphone="222222", email="1@mail.ru", email2="2@mail.ru", email3="3@mail.ru")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(first_name="", middle_name="", last_name="",
#                            nick_name="", title="", company="", address="",
#                            home_phone="", mobile_phone="", work_phone="", fax_phone="",
#                            email="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

