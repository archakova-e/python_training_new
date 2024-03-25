# -*- coding: utf-8 -*-
from model.contact_properties import ContactProperties


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactProperties(firstname="Ivan", middlename="Ivanich", lastname="Ivanov", nickname="ivanka",
                                title="Test", company="Test", address="Test 8-2-168", home_phone="65124",
                                mobile_phone="90523245678", work_phone="3252525", fax="2222222", email="iva@mail.com",
                                email2="iva2@mail.com", email3="iva3@mail.com", homepage="www.iva.com", bday="10",
                                bmonth="November", aday="10", amonth="November")
    app.contact.add_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactProperties.id_or_max) == \
           sorted(new_contacts, key=ContactProperties.id_or_max)
