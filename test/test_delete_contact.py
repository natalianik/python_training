__author__ = 'Natalia.Nikonova'

def test_delete_first_contact(app):
    app.contact.delete_first_contact()
