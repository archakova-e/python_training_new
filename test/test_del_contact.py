from model.contact_properties import ContactProperties

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_contact_properties(ContactProperties(firstname="test"))
    app.contact.delete_first_contact()