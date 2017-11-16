# -*- coding: utf-8 -*-
from model.contact import Contact



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
        self.change_field_value("firstname",contact.first_name)
        self.change_field_value("middlename",contact.middle_name)
        self.change_field_value("lastname",contact.last_name)
        self.change_field_value("nickname",contact.nick_name)
        self.change_field_value("title",contact.title)
        self.change_field_value("company",contact.company)
        self.change_field_value("address",contact.address)
        self.change_field_value("home",contact.home_phone)
        self.change_field_value("mobile",contact.mobile_phone)
        self.change_field_value("work",contact.work_phone)
        self.change_field_value("fax",contact.fax_phone)
        self.change_field_value("email",contact.email)

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

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                columns = element.find_elements_by_tag_name("td")
                id = columns[0].find_element_by_tag_name("input").get_attribute("value")
                first_name = columns[2].text
                self.contact_cache.append(Contact(first_name=first_name, id=id))
        return list(self.contact_cache)



