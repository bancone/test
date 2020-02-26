# -*- coding: utf-8 -*-
import pytest
from fixture.rpapp import RPApp


@pytest.fixture(scope="session")
def rpapp(request):
    fixture = RPApp()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_register_person(rpapp):
    rpapp.session.login()
    rpapp.register_person.create_docs(email="s.pobedinskiy+2002251@iconic.vc")
    rpapp.create_account.auth_to_gmail()
    rpapp.create_account.set_password(password="1234567890qwerty!")


def test_create_identity_docs(rpapp):
    rpapp.session.login()
    rpapp.create_identity_docs.create_docs()


def test_create_address_bill(rpapp):
    rpapp.session.login()
    rpapp.create_address_bill.create_docs()


def test_create_selfie(rpapp):
    rpapp.session.login()
    rpapp.create_selfie.create_docs()


def test_create_SOW(rpapp):
    rpapp.session.login()
    rpapp.create_SOW.create_docs()


def test_create_test(rpapp):
    rpapp.session.login()
    rpapp.create_test.create_docs()


#def test_approve_documents(rpapp):
#    rpapp.session.login_ex()
#    rpapp.approve_documents.approve_documents()
