import string
import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.Properties import Config
from Utilities.customLogger import LogGen
from pageObjects.AddcustomerPage import AddCustomer
import random

class Test003_Login:
    baseURL = Config.BaseURL()
    username = Config.GetUsername()
    password = Config.GetPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.driver = setup
        self.logger.info("******Test003_Login******")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.adcust=AddCustomer(self.driver)

        self.adcust.clickonCustomerMenu()
        self.adcust.clickonCustomerMenuItems()

        self.adcust.clickonAddnew()
        self.email=random_generator() + "@gmail.com"
        self.adcust.setEmail(self.email)
        time.sleep(1)
        self.adcust.setPassword('test123')
        time.sleep(1)
        self.adcust.setMangervendor('Vendor 2')
        time.sleep(1)
        self.adcust.setGender('Male')
        time.sleep(1)
        self.adcust.setfirstName("Automation")
        time.sleep(1)
        self.adcust.setlastName("Tester")
        time.sleep(1)
        self.adcust.clickonDOB("24/11/1998")
        time.sleep(1)
        self.adcust.setcompanyName('AMR')
        time.sleep(1)
        self.adcust.setAdmincontent("login is successfully")
        time.sleep(1)
        self.adcust.saveonclick()

        self.driver.close()
def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
