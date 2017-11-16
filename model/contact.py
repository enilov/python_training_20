# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None,
                 address=None,homephone=None, mobilephone=None, workphone=None, email=None,
                 id = None,
                 secondaryphone=None, all_phones_from_home_page=None,
                 email2=None, email3=None, all_emails_from_home_page=None ):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email = email
        self.id = id
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

