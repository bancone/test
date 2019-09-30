from selenium import webdriver
from fixture.session import SessionHelper
from fixture.create_identity_docs import CreateID
from fixture.create_address_bill import CreateAB
from fixture.create_selfie import CreateS
from fixture.register_person import RegisterP
from fixture.create_SOW import CreateSOW
from fixture.create_test import CreateT


class RPApp:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.create_identity_docs = CreateID(self)
        self.create_address_bill = CreateAB(self)
        self.create_selfie = CreateS(self)
        self.register_person = RegisterP(self)
        self.create_SOW = CreateSOW(self)
        self.create_test = CreateT(self)

    def destroy(self):
        self.driver.quit()
