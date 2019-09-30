# coding=utf-8
import time
import os


class CreateID:

    def __init__(self, rpapp):
        self.rpapp = rpapp

    def create_docs(self):
        driver = self.rpapp.driver
        driver.set_window_size(1920, 1080)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='ti'])[1]/following::button[6]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='RUS'])[1]/following::td[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath('//button[text()="Create Identity Document"]').click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Document Type'])[1]/following::div[3]").click()
        driver.implicitly_wait(20)
        driver.find_element_by_id("react-select-7-option-2").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='File'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='File'])[1]/preceding::input[1]").send_keys(os.getcwd() + "/111.png")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='File'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create Identity Document'])[1]/preceding::a[1]").click()
        driver.find_element_by_xpath("//a[contains(@href, '/client')]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='ro'])[1]/following::button[1]").click()