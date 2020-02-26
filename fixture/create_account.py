import time
from selenium.webdriver.common.keys import Keys
import pyotp


class CreateAcc:

    def __init__(self, rpapp):
        self.rpapp = rpapp
        self.totp_secret = "7vqjehxzpc3heineh6r3iewgcj7yuh4r"

    def login_bro(self, email, password):
        self.open_broker()
        self.open_broker_signin()
        self.fill_field(email)
#        self.first_fill_registration()
        self.auth_to_gmail()
        self.set_password(password)
        self.auth(email, password)

    def get_totp(self):
            totp = pyotp.TOTP(self.totp_secret)
            return totp.now()

    def auth(self, email, password):
        driver = self.rpapp.driver
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("%s" % password)
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def set_password(self, password):
        driver = self.rpapp.driver
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys("%s" % password)
        driver.find_element_by_name("passwordConfirmation").click()
        driver.find_element_by_name("passwordConfirmation").send_keys("%s" % password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Confirm Password'])[1]/following::button[1]").click()

    def auth_to_gmail(self):
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
            u"'Слишком много неудачных попыток'])[1]/following::span[8]").click()
        driver.find_element_by_name("totpPin").clear()
        driver.find_element_by_name("totpPin").send_keys(self.get_totp())
        driver.find_element_by_xpath("//div[@id='totpNext']/span/span").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='zubr.io Development'])[2]/following::span[2]").click()
        driver.find_element_by_link_text("VERIFY EMAIL").click()
        driver.switch_to.window(driver.window_handles[1])

 #   def first_fill_registration(self):
 #       driver = self.rpapp.driver
  #      driver.find_element_by_xpath(
  #          "(.//*[normalize-space(text()) and normalize-space(.)='Russian Federation'])[1]/following::span[2]").click()
  #      driver.find_element_by_xpath(
  #          "(.//*[normalize-space(text()) and normalize-space(.)='privacy agreement'])[1]/following::span[1]").click()

    def fill_field(self, email):
        driver = self.rpapp.driver
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("%s" % email)
        driver.find_element_by_css_selector("div._suggest__value-container.css-1hwfws3").click()
        driver.find_element_by_xpath("//div/div/input").send_keys("Russian Federation (the)")
        driver.find_element_by_xpath("//div/div/input").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//div[3]/div/label/div").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def open_broker_signin(self):
        driver = self.rpapp.driver
        time.sleep(1)
        driver.find_element_by_xpath("(.//*[normalize-space(text())"
                                     " and normalize-space(.)='Login'])[1]/following::button[1]").click()

    def open_broker(self):
        driver = self.rpapp.driver
        driver.get("https://broker-sandbox-front.zubr.tech/")
        driver.set_window_size(1920, 1080)

    def test(self, password):
        driver = self.rpapp.driver
        self.auth_to_gmail()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_name("password").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Please set a password.'])"
            "[1]/following::input[1]").send_keys("%s" % password)
        driver.find_element_by_name("passwordConfirm").click()
        driver.find_element_by_name("passwordConfirm").send_keys("%s" % password)
