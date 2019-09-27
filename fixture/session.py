

class SessionHelper:

    def __init__(self, rpapp):
        self.rpapp = rpapp

    def login(self):
        driver = self.rpapp.driver
        self.rpapp.open_bro0()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("root")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("root")
        driver.find_element_by_xpath("//button[@type='submit']").click()
