# coding=utf-8
import time
import os


class ApproveDocs:

    def __init__(self, rpapp):
        self.rpapp = rpapp

    def approve_documents(self):
        driver = self.rpapp.driver
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='id'])[1]/following::button[3]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='RUS'])[1]/following::td[1]").click()
        time.sleep(3)
        #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Client 2793 Details'])[1]/preceding::a[1]").click()
