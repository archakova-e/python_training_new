from model.contact_properties import ContactProperties


def test_1_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(firstname="test"))
    app.contact.modify_first_contact(ContactProperties(firstname="Petr"))


def test_2_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties())
    app.contact.modify_first_contact(ContactProperties(firstname="Petr"))


def test_3_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(firstname="test"))
    app.contact.modify_first_contact(ContactProperties())


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(middlename="test"))
    app.contact.modify_first_contact(ContactProperties(middlename="Petrovich"))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(lastname="test"))
    app.contact.modify_first_contact(ContactProperties(lastname="Petrov"))


def test_modify_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(nickname="test"))
    app.contact.modify_first_contact(ContactProperties(nickname="petrushka"))


def test_modify_contact_title(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(title="test"))
    app.contact.modify_first_contact(ContactProperties(title="Test_1"))


def test_modify_contact_company(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(company="test"))
    app.contact.modify_first_contact(ContactProperties(company="Test_1"))


def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(address="test"))
    app.contact.modify_first_contact(ContactProperties(address="Test 8-2-169"))


def test_modify_contact_home(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(home_phone="test"))
    app.contact.modify_first_contact(ContactProperties(home_phone="23230"))


def test_modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(mobile_phone="test"))
    app.contact.modify_first_contact(ContactProperties(mobile_phone="9051234567"))


def test_modify_contact_work(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(work_phone="test"))
    app.contact.modify_first_contact(ContactProperties(work_phone="3262626"))


def test_modify_contact_fax(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(fax="test"))
    app.contact.modify_first_contact(ContactProperties(fax="3333333"))


def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(email="test"))
    app.contact.modify_first_contact(ContactProperties(email="petr@mail.com"))


def test_modify_contact_email2(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(email2="test"))
    app.contact.modify_first_contact(ContactProperties(email2="petr2@mail.com"))


def test_modify_contact_email3(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(email3="test"))
    app.contact.modify_first_contact(ContactProperties(email3="petr3@mail.com"))


def test_modify_contact_homepage(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(homepage="test"))
    app.contact.modify_first_contact(ContactProperties(homepage="www.petr.com"))


def test_modify_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(bday="10"))
    app.contact.modify_first_contact(ContactProperties(bday="15"))


def test_modify_contact_bmonth(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(bmonth="November"))
    app.contact.modify_first_contact(ContactProperties(bmonth="December"))


def test_modify_contact_aday(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(aday="10"))
    app.contact.modify_first_contact(ContactProperties(aday="15"))


def test_modify_contact_amonth(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(amonth="November"))
    app.contact.modify_first_contact(ContactProperties(amonth="December"))
