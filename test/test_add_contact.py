# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    test_contact = Contact(first_name="name", middle_name="mid_name", last_name="last_name",
                           nick_name="nick_name", title="title", company="company", address="address",
                           home_phone="123", mobile_phone="321", work_phone="456", fax_phone="654",
                           email="1@mail.ru")
    app.contact.create(test_contact)

def test_add_empty_contact(app):
    test_contact = Contact(first_name="", middle_name="", last_name="",
                           nick_name="", title="", company="", address="",
                           home_phone="", mobile_phone="", work_phone="", fax_phone="",
                           email="")
    app.contact.create(test_contact)
