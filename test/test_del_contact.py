# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_delete_first_contact(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = db.get_contact_list()
    # assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


