# -*- coding: utf-8 -*-
import pytest
from contact_properties import ContactProperties
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.fill_contact_properties(ContactProperties(firstname="Ivan", middlename="Ivanich", lastname="Ivanov",
                                                  nickname="ivanka", title="Test", company="Test",
                                                  address="Test 8-2-168", home_phone="65124",
                                                  mobile_phone="90523245678", work_phone="3252525",
                                                  fax="2222222", email="iva@mail.com", email2="iva2@mail.com",
                                                  email3="iva3@mail.com", homepage="www.iva.com", bday="10",
                                                  bmonth="November", aday="10", amonth="November"))
    app.logout()
