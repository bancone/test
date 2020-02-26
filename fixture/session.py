

class SessionHelper:

    def __init__(self, rpapp):
        self.rpapp = rpapp

    def login(self):
        driver = self.rpapp.driver
        self.open_bro0()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("root")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("root")
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def open_bro0(self):
        driver = self.rpapp.driver
        driver.get("http://br0-admin-demo.iconic.local/login")
        driver.set_window_size(1920, 1080)

    def logout(self):
        driver = self.rpapp.driver
        driver.get("http://br0-admin-demo.iconic.local/client")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ro'])[1]/following::button[1]").click()
        driver.quit()

    def login_ex(self):
        driver = self.rpapp.driver
        self.open_ex()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("root@root.root")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("aDASFDFSdasd")
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def open_ex(self):
        driver = self.rpapp.driver
        driver.get("http://exchange-admin-demo.iconic.local/login")
        driver.set_window_size(1920, 1080)

    def logout_ex(self):
        driver = self.rpapp.driver
        driver.get("http://exchange-admin-demo.iconic.local/client")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ro'])[1]/following::button[1]").click()
        driver.quit()
