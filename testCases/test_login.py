import pytest
import logging
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.Properties import Config
from Utilities.customLogger import LogGen


class Test001_Login:
    baseURL = Config.BaseURL()
    username = Config.GetUsername()
    password = Config.GetPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("******Verify the homepageTitle*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("******homepageTitle is passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.logger.info("******Test001_Login******")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            assert False
        self.logger.info("**** login successfully ****")