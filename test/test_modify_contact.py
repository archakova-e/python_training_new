from model.contact_properties import ContactProperties


def test_modify_first_contact(app):
    app.session.login(username="Admin", password="secret")
    app.contact.modify_first_contact(ContactProperties(firstname="Petr", middlename="Petrovich", lastname="Petrov",
                                                       nickname="petrushka", title="Test_1", company="Test_1",
                                                       address="Test 8-2-169", home_phone="23230",
                                                       mobile_phone="9051234567", work_phone="3262626",
                                                       fax="3333333", email="petr@mail.com", email2="petr@mail.com",
                                                       email3="petr3@mail.com", homepage="www.petr.com", bday="15",
                                                       bmonth="December", aday="15", amonth="December"))
    app.session.logout()
