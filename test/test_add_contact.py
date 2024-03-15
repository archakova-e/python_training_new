# -*- coding: utf-8 -*-
from model.contact_properties import ContactProperties


def test_add_contact(app):
    app.contact.fill_contact_properties(ContactProperties(firstname="Ivan", middlename="Ivanich", lastname="Ivanov",
                                                          nickname="ivanka", title="Test", company="Test",
                                                          address="Test 8-2-168", home_phone="65124",
                                                          mobile_phone="90523245678", work_phone="3252525",
                                                          fax="2222222", email="iva@mail.com", email2="iva2@mail.com",
                                                          email3="iva3@mail.com", homepage="www.iva.com", bday="10",
                                                          bmonth="November", aday="10", amonth="November"))
