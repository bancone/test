from selenium import webdriver

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def call_operator_form(self):
        driver = self.driver
        # call operator form
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ti'])[1]/following::button[7]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Operators'])[1]/following::button[1]").click()

    def login_br0(self):
        driver = self.driver
        self.open_br0()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("root")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("root")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()

    def filling_create_operator_form(self, email):
        driver = self.driver
        self.call_operator_form()
        # filling form
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("%s" % email)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("111111111")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Role'])[1]/following::div[4]").click()
        driver.find_element_by_xpath("//div[@id='react-select-5-option-1']").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Broker Admin'])[2]/following::button[1]").click()

    def open_br0(self):
        driver = self.driver
        driver.get("http://br0-admin.test7.iconic.local:81/login")

    def destroy(self):
        self.driver.quit()
