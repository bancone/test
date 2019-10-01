import time


class CreateAcc:

    def __init__(self, rpapp):
        self.rpapp = rpapp

    def login_bro(self, email):
        driver = self.rpapp.driver
        self.open_broker()
        self.open_broker_signin()
        self.fill_field(email)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Russian Federation'])[1]/following::span[2]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='privacy agreement'])[1]/following::span[1]").click()
        driver.get("https://mail.google.com/mail/u/0/#inbox")
        driver.find_element_by_id("identifierId").clear()
        driver.find_element_by_id("identifierId").send_keys("s.pobedinskiy@iconic.vc")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробнее…'])[1]/following::span[2]").click()
        time.sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("1234567q-")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)="
            u"'Слишком много неудачных попыток'])[1]/following::span[8]")\
            .click()
        time.sleep(2)
        time.sleep(3)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='zubr.io Development'])[2]/following::span[2]").click()
        driver.find_element_by_link_text("VERIFY EMAIL").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys("1234qwer")
        driver.find_element_by_name("passwordConfirm").click()
        driver.find_element_by_name("passwordConfirm").send_keys("1234qwer")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Confirm Password'])[1]/following::button[1]").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("1234qwer")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='I forgot password'])[1]/following::button[1]")\
            .click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::div[2]").click()

    def fill_field(self, email):
        driver = self.rpapp.driver
        driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div/a/span").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("%s" % email)
        driver.find_element_by_id("react-select-2-input").clear()
        driver.find_element_by_id("react-select-2-input").send_keys("Russian Federation")
        driver.find_element_by_id("react-select-2-option-182").click()

    def open_broker_signin(self):
        driver = self.rpapp.driver
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/a/span').click()

    def open_broker(self):
        driver = self.rpapp.driver
        driver.get("http://test7.iconic.local/")
        driver.set_window_size(1920, 1080)

    def test(self):
        driver = self.rpapp.driver
        driver.get("https://mail.google.com/mail/u/0/#inbox")
        driver.find_element_by_id("identifierId").clear()
        driver.find_element_by_id("identifierId").send_keys("s.pobedinskiy@iconic.vc")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Подробнее…'])[1]/following::span[2]").click()
        time.sleep(1)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("1234567q-")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)="
            u"'Слишком много неудачных попыток'])[1]/following::span[8]")\
            .click()
        time.sleep(2)
        time.sleep(3)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='zubr.io Development'])[2]/following::span[2]").click()
        driver.find_element_by_link_text("VERIFY EMAIL").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_name("password").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please set a password.'])"
            "[1]/following::input[1]").send_keys("1234qwer")
        driver.find_element_by_name("passwordConfirm").click()
        driver.find_element_by_name("passwordConfirm").send_keys("1234qwer")