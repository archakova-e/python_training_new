from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_calendary(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact_properties):
        wd = self.app.wd
        self.change_field_value("firstname", contact_properties.firstname)
        self.change_field_value("middlename", contact_properties.middlename)
        self.change_field_value("lastname", contact_properties.lastname)
        self.change_field_value("nickname", contact_properties.nickname)
        self.change_field_value("title", contact_properties.title)
        self.change_field_value("company", contact_properties.company)
        self.change_field_value("address", contact_properties.address)
        self.change_field_value("home", contact_properties.home_phone)
        self.change_field_value("mobile", contact_properties.mobile_phone)
        self.change_field_value("work", contact_properties.work_phone)
        self.change_field_value("fax", contact_properties.fax)
        self.change_field_value("email", contact_properties.email)
        self.change_field_value("email2", contact_properties.email2)
        self.change_field_value("email3", contact_properties.email3)
        self.change_field_value("homepage", contact_properties.homepage)
        self.change_field_value_calendary("bday", contact_properties.bday)
        self.change_field_value_calendary("bmonth", contact_properties.bmonth)
        self.change_field_value_calendary("aday", contact_properties.aday)
        self.change_field_value_calendary("amonth", contact_properties.amonth)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def submit_modification(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def delete_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def add_new_contact(self, contact_properties):
        self.open_add_contact_page()
        self.fill_contact_form(contact_properties)

    def modify_first_contact(self, new_contact_data):
        self.open_contact_page()
        self.edit_contact()
        self.fill_contact_form(new_contact_data)
        self.submit_modification()

    def delete_first_contact(self):
        self.open_contact_page()
        self.select_first_contact()
        self.delete_button()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))
