# coding=utf-8
import time


class CreateT:

    def __init__(self, rpapp):
        self.rpapp = rpapp

    def create_docs(self):
        driver = self.rpapp.driver
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ti'])[1]/following::button[6]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='RUS'])[1]/following::td[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath('//button[text()="Create Qualification Test Document"]').click()
        driver.find_element_by_xpath('//button[text()="Create Qualification Test Document"]').click()
        driver.find_element_by_xpath(
            "//a[contains(@href, '/client')]").click()
