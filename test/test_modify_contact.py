from model.contact_properties import ContactProperties


def test_1_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(firstname="test"))
    contact = ContactProperties(lastname="Karmanov", firstname="Karman")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactProperties.id_or_max) == \
           sorted(new_contacts, key=ContactProperties.id_or_max)


def test_2_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties())
    app.contact.modify_first_contact(ContactProperties(firstname="Petr"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_3_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(firstname="test"))
    app.contact.modify_first_contact(ContactProperties())
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_middlename(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(middlename="test"))
    app.contact.modify_first_contact(ContactProperties(middlename="Petrovich"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_lastname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(lastname="test"))
    app.contact.modify_first_contact(ContactProperties(lastname="Petrov"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_nickname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(nickname="test"))
    app.contact.modify_first_contact(ContactProperties(nickname="petrushka"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_title(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(title="test"))
    app.contact.modify_first_contact(ContactProperties(title="Test_1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_company(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(company="test"))
    app.contact.modify_first_contact(ContactProperties(company="Test_1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_address(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(address="test"))
    app.contact.modify_first_contact(ContactProperties(address="Test 8-2-169"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_home(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(home_phone="test"))
    app.contact.modify_first_contact(ContactProperties(home_phone="23230"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_mobile(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(mobile_phone="test"))
    app.contact.modify_first_contact(ContactProperties(mobile_phone="9051234567"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_work(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(work_phone="test"))
    app.contact.modify_first_contact(ContactProperties(work_phone="3262626"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_fax(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(fax="test"))
    app.contact.modify_first_contact(ContactProperties(fax="3333333"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_email(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(email="test"))
    app.contact.modify_first_contact(ContactProperties(email="petr@mail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_email2(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(email2="test"))
    app.contact.modify_first_contact(ContactProperties(email2="petr2@mail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_email3(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(email3="test"))
    app.contact.modify_first_contact(ContactProperties(email3="petr3@mail.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_homepage(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(homepage="test"))
    app.contact.modify_first_contact(ContactProperties(homepage="www.petr.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_bday(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(bday="10"))
    app.contact.modify_first_contact(ContactProperties(bday="15"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_bmonth(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(bmonth="November"))
    app.contact.modify_first_contact(ContactProperties(bmonth="December"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_aday(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(aday="10"))
    app.contact.modify_first_contact(ContactProperties(aday="15"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_amonth(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.add_new_contact(ContactProperties(amonth="November"))
    app.contact.modify_first_contact(ContactProperties(amonth="December"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
