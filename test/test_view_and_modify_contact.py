# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    test_contact = Contact(first_name="name", middle_name="mid_name", last_name="last_name",
                           nick_name="nick_name", title="title", company="company", address="address",
                           home_phone="123", mobile_phone="321", work_phone="456", fax_phone="654",
                           email="1@mail.ru", born_year="2001",
                           born_day="//div[@id='content']/form/select[1]//option[3]",
                           born_month="//div[@id='content']/form/select[2]//option[2]")
    app.contact.view_details_and_modify_first(test_contact)
    app.session.logout()
