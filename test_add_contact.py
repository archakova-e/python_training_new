# -*- coding: utf-8 -*-
import unittest
import pytest
from contact_properties import ContactProperties
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# class TestAddContact(unittest.TestCase):
#     def setUp(self):
#         self.wd = webdriver.Firefox()
#         self.wd.implicitly_wait(30)

    # def open_add_page(self):
    #     wd = self.wd
    #     wd.get("http://localhost/addressbook/edit.php")

    # def login(self, username, password):
    #     wd = self.wd
    #     self.open_add_page()
    #     wd.find_element_by_name("user").clear()
    #     wd.find_element_by_name("user").send_keys(username)
    #     wd.find_element_by_name("pass").click()
    #     wd.find_element_by_name("pass").clear()
    #     wd.find_element_by_name("pass").send_keys(password)
    #     wd.find_element_by_xpath("//input[@value='Login']").click()

    # def fill_contact_properties(self, contact_properties):
    #     wd = self.wd
    #     # fill contact names
    #     wd.find_element_by_name("firstname").click()
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys(contact_properties.firstname)
    #     wd.find_element_by_name("middlename").click()
    #     wd.find_element_by_name("middlename").clear()
    #     wd.find_element_by_name("middlename").send_keys(contact_properties.middlename)
    #     wd.find_element_by_name("lastname").click()
    #     wd.find_element_by_name("lastname").clear()
    #     wd.find_element_by_name("lastname").send_keys(contact_properties.lastname)
    #     wd.find_element_by_name("nickname").click()
    #     wd.find_element_by_name("nickname").clear()
    #     wd.find_element_by_name("nickname").send_keys(contact_properties.nickname)
    #     # fill contact location
    #     wd.find_element_by_name("title").click()
    #     wd.find_element_by_name("title").clear()
    #     wd.find_element_by_name("title").send_keys(contact_properties.title)
    #     wd.find_element_by_name("company").click()
    #     wd.find_element_by_name("company").clear()
    #     wd.find_element_by_name("company").send_keys(contact_properties.company)
    #     wd.find_element_by_name("address").click()
    #     wd.find_element_by_name("address").clear()
    #     wd.find_element_by_name("address").send_keys(contact_properties.address)
    #     # fill contact phones
    #     wd.find_element_by_name("home").click()
    #     wd.find_element_by_name("home").clear()
    #     wd.find_element_by_name("home").send_keys(contact_properties.home_phone)
    #     wd.find_element_by_name("mobile").click()
    #     wd.find_element_by_name("mobile").clear()
    #     wd.find_element_by_name("mobile").send_keys(contact_properties.mobile_phone)
    #     wd.find_element_by_name("work").click()
    #     wd.find_element_by_name("work").clear()
    #     wd.find_element_by_name("work").send_keys(contact_properties.work_phone)
    #     wd.find_element_by_name("fax").click()
    #     wd.find_element_by_name("fax").clear()
    #     wd.find_element_by_name("fax").send_keys(contact_properties.fax)
    #     # fill contact emails and homepage
    #     wd.find_element_by_name("email").click()
    #     wd.find_element_by_name("email").clear()
    #     wd.find_element_by_name("email").send_keys(contact_properties.email)
    #     wd.find_element_by_name("email2").click()
    #     wd.find_element_by_name("email2").clear()
    #     wd.find_element_by_name("email2").send_keys(contact_properties.email2)
    #     wd.find_element_by_name("email3").click()
    #     wd.find_element_by_name("email3").clear()
    #     wd.find_element_by_name("email3").send_keys(contact_properties.email3)
    #     wd.find_element_by_name("homepage").click()
    #     wd.find_element_by_name("homepage").clear()
    #     wd.find_element_by_name("homepage").send_keys(contact_properties.homepage)
    #     # fill contact birthday
    #     wd.find_element_by_name("bday").click()
    #     Select(wd.find_element_by_name("bday")).select_by_visible_text(contact_properties.bday)
    #     wd.find_element_by_xpath("//option[@value='10']").click()
    #     wd.find_element_by_name("bmonth").click()
    #     Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact_properties.bmonth)
    #     wd.find_element_by_xpath("//option[@value='November']").click()
    #     wd.find_element_by_name("aday").click()
    #     Select(wd.find_element_by_name("aday")).select_by_visible_text(contact_properties.aday)
    #     wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[12]").click()
    #     wd.find_element_by_name("amonth").click()
    #     Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact_properties.amonth)
    #     wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[12]").click()
    #     wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    # def logout(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("Logout").click()


def test_add_contact(app):
    app.login(username="Admin", password="secret")
    app.fill_contact_properties(ContactProperties(firstname="Ivan", middlename="Ivanich", lastname="Ivanov",
                                                           nickname="ivanka", title="Test", company="Test",
                                                           address="Test 8-2-168", home_phone="65124",
                                                           mobile_phone="90523245678", work_phone="3252525",
                                                           fax="2222222", email="iva@mail.com", email2="iva2@mail.com",
                                                           email3="iva3@mail.com", homepage="www.iva.com", bday="10",
                                                           bmonth="November", aday="10", amonth="November"))
    app.logout()

    # def test_add_contact(self):
    #     #wd = self.wd
    #     #self.open_add_page(wd)
    #     self.login(username="admin", password="secret")
    #     self.fill_contact_properties(ContactProperties(firstname="Ivan", middlename="Ivanich", lastname="Ivanov",
    #                                                        nickname="ivanka", title="Test", company="Test",
    #                                                        address="Test 8-2-168", home_phone="65124",
    #                                                        mobile_phone="90523245678", work_phone="3252525",
    #                                                        fax="2222222", email="iva@mail.com", email2="iva2@mail.com",
    #                                                        email3="iva3@mail.com", homepage="www.iva.com", bday="10",
    #                                                        bmonth="November", aday="10", amonth="November"))
    #     self.logout()

#     def tearDown(self):
#         self.wd.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()
