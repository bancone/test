# -*- coding: utf-8 -*-
import pytest
from fixture.rpapp import RPApp
from datetime import datetime


@pytest.fixture(scope="session")
def rpapp(request):
    fixture = RPApp()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_account(rpapp):
    rpapp.create_account.login_bro(email=f's.pobedinskiy+{datetime.today().strftime("%y%m%d%H%M%S")}@iconic.vc', password="1234567890qwerty!")
    #rpapp.create_qt.start_test(email="s.pobedinskiy+2002251@iconic.vc", password="1234567890qwerty!")