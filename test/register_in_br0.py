# -*- coding: utf-8 -*-
import pytest
from fixture.rpapp import RPApp


@pytest.fixture(scope="session")
def rpapp(request):
    fixture = RPApp()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_account(rpapp):
    rpapp.create_account.login_bro(email="s.pobedinskiy+19100124@iconic.vc")
    #rpapp.create_account.test()