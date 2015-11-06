__author__ = 'Natalia.Nikonova'
import pytest
from model.contact import contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(contact(firstname="Natalya", middlename="Valerievna", lastname="Nikonova",
                    nickname="natalian", title="engineer", company="Peter-Service", address="Ekaterinburg", home="343",
                    mobile="953", work="3107046", fax="3107048", email="natalia.nikonova@billing.ru", email2="\\9",
                    homepage="www.billing.ru", byear="1977", address2="Yekaterinburg", phone2="13",
                    notes="comment for this contact"))
    app.session.logout()