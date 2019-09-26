# -*- coding: utf-8 -*-
import pytest
from application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.login_br0()
    app.filling_create_operator_form("111+15@11111.11")

