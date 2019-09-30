# -*- coding: utf-8 -*-
import pytest
from fixture.rpapp import RPApp


@pytest.fixture(scope="session")
def rpapp(request):
    fixture = RPApp()
    request.addfinalizer(fixture.destroy)
    return fixture


#def test_register_person(rpapp):
#    rpapp.session.login()
#    rpapp.register_person(email="s.pobedinskiy+19092717@iconic.vc")

def test_create_identity_docs(rpapp):
    rpapp.session.login()
    rpapp.create_identity_docs.create_docs()
