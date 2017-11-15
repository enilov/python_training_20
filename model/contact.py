# -*- coding: utf-8 -*-


class Contact:
    def __init__(self,first_name=None, middle_name=None, last_name=None,
                 nick_name=None, title=None, company=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, fax_phone=None, email=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.email = email
