# -*- coding: utf-8 -*-
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # add new contact and fill some fields
        # init group creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value("firstname",contact.firstname)
        self.change_field_value("middlename",contact.middlename)
        self.change_field_value("lastname",contact.lastname)
        self.change_field_value("address",contact.address)
        self.change_field_value("home",contact.homephone)
        self.change_field_value("mobile",contact.mobilephone)
        self.change_field_value("work",contact.workphone)
        self.change_field_value("email",contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("phone2", contact.secondaryphone)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        # we login on page with contacts
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.select_contact_by_index(index)
        # submit deletition
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        alert = wd.switch_to_alert()
        # sometimes alert is not accepted in my browser :(
        try:
            alert.accept()
            alert.accept()
            alert.accept()
            alert.accept()
        except:
            pass
        self.contact_cache = None

    def modify_group_by_index(self, index, new_contact_data):
        # we login on page with contacts
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.select_contact_by_index(index)
        # edit
        wd.find_element_by_xpath("// table[ @ id = 'maintable'] / tbody / tr[2] / td[8] / a / img").click()
        self.fill_contact_form(new_contact_data)
        # submit
        wd.find_element_by_xpath("// div[ @ id = 'content'] / form[1] / input[22]").click()
        self.contact_cache = None


    def edit_first_contact(self, new_contact_data):
        self.modify_group_by_index(0, new_contact_data)

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def view_details_and_modify_first(self,new_contact_data):
        # we login on page with contacts
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.select_first_contact()
        # view
        wd.find_element_by_xpath("// table[ @ id = 'maintable'] / tbody / tr[2] / td[7] / a / img").click()
        # modify
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(new_contact_data)
        # submit
        wd.find_element_by_xpath("// div[ @ id = 'content'] / form[1] / input[22]").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def add_first_contact_to_first_group(self):
        # we login on page with contacts
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.select_first_contact()
        # add to first group
        wd.find_element_by_name("add").click()
        # go to group page
        wd.find_element_by_xpath("//div/div[4]/div/i/a")

    contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                columns = element.find_elements_by_tag_name("td")
                id = columns[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = columns[1].text
                firstname = columns[2].text
                all_emails = columns[4].text
                all_phones = columns[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                       secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                       secondaryphone=secondaryphone)







