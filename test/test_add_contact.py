# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    test_contact = Contact(first_name="name", middle_name="mid_name", last_name="last_name",
                           nick_name="nick_name", title="title", company="company", address="address",
                           home_phone="123", mobile_phone="321", work_phone="456", fax_phone="654",
                           email="1@mail.ru", born_year="2001",
                           born_day="//div[@id='content']/form/select[1]//option[3]",
                           born_month="//div[@id='content']/form/select[2]//option[2]")
    app.contact.add_new(test_contact)
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    test_contact = Contact(first_name="", middle_name="", last_name="",
                           nick_name="", title="", company="", address="",
                           home_phone="", mobile_phone="", work_phone="", fax_phone="",
                           email="", born_year="",
                           born_day="//div[@id='content']/form/select[1]//option[3]",
                           born_month="//div[@id='content']/form/select[2]//option[2]")
    app.contact.add_new(test_contact)
    app.session.logout()
