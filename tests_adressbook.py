# -*- coding: utf-8 -*-
import pytest
from group import Group
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# test add group
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="group1", header="group1", footer="group1"))
    app.logout()


# test add empty group
def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


# test add contact
def test_test_add_contact(app):
    app.login(username="admin", password="secret")
    test_contact = Contact(first_name="name", middle_name="mid_name", last_name="last_name",
                           nick_name="nick_name", title="title", company="company", address="address",
                           home_phone="123", mobile_phone="321", work_phone="456", fax_phone="654",
                           email="1@mail.ru", born_year="2001",
                           born_day="//div[@id='content']/form/select[1]//option[3]",
                           born_month="//div[@id='content']/form/select[2]//option[2]")
    app.add_new_contact(test_contact)
    app.logout()
