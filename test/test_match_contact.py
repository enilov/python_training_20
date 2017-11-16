import re
from random import randrange

def test_match_on_home_page(app):
    contacts = app.contact.get_contact_list()
    i = randrange(len(contacts))
    contact_from_homepage = app.contact.get_contact_list()[i]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.middlename == contact_from_edit_page.middlename
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.id == contact_from_edit_page.id
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

    a = contact_from_homepage.all_emails_from_home_page
    b = merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
            map(lambda x: clear(x),
                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))