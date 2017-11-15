# -*- coding: utf-8 -*-

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_first_contact_to_first_group()
    app.session.logout()
