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
    rpapp.register_person.create_docs(email="s.pobedinskiy+1910016@iconic.vc")


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
