__author__ = 'Natalia.Nikonova'

from model.contact import contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(contact(firstname="Natalia", middlename="V.", lastname="Nikonova",
                    nickname="natalian", title="engineer", company="PS", address="Yekaterinburg", home="343",
                    mobile="953", work="3107046", fax="3107048", email="natalia.nikonova@billing.ru", email2="\\9",
                    homepage="www.billing.ru", byear="1977", address2="Yekaterinburg", phone2="13",
                    notes="comment for contact"))
    app.contact.edit_first(contact(firstname="Natalya", middlename="Valerievna", lastname="Nikonova",
                    nickname="natalian", title="engineer", company="Peter-Service", address="Ekaterinburg", home="343",
                    mobile="953", work="3107046", fax="3107048", email="natalia.nikonova@billing.ru", email2="None",
                    homepage="www.billing.ru", byear="1977", address2="Yekaterinburg", phone2="13",
                    notes="comment for this contact"))