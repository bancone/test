# -*- coding: utf-8 -*-
import pytest
from fixture.rpapp import RPApp


@pytest.fixture()
def rpapp(request):
    fixture = RPApp()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_register_person(rpapp):
    rpapp.open_bro0()
    rpapp.login()
    rpapp.register_person(email="s.pobedinskiy+1909276@iconic.vc")
