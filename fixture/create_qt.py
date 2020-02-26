import time


class Createqt:

    def __init__(self, rpapp):
        self.rpapp = rpapp

    def start_test(self, email, password):
        driver = self.rpapp.driver
        driver.get("https://broker-sandbox-front.zubr.tech/")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("%s" % password)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Last price'])[1]/following::button[3]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Wallet'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)="
                                     "'Please complete trading test'])[1]/following::button[1]").click()
        time.sleep(2)
