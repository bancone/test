

class RegisterP:

    def __init__(self, rpapp):
        self.rpapp = rpapp

    def register_person(self, email):
        driver = self.rpapp.driver
        # Open client page
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='ti'])[1]/following::button[6]").click()
        # Register person
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Clients'])[1]/following::button[1]").click()
        # empty
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Create Client'])[1]/following::div[7]").click()
        # Full
        driver.find_element_by_name("dateOfBirth").clear()
        driver.find_element_by_name("dateOfBirth").send_keys("2001.01.01")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("%s" % email)
        driver.find_element_by_name("firstName").clear()
        driver.find_element_by_name("firstName").send_keys("Sergey")
        driver.find_element_by_name("lastName").clear()
        driver.find_element_by_name("lastName").send_keys("Pobedinskiy")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Create Client'])[1]/following::form[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Residency'])[1]/following::div[3]").click()
        driver.find_element_by_id("react-select-5-option-0").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='RUS'])[1]/following::button[1]").click()
