import time
import openpyxl
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.Properties import Config
from Utilities.customLogger import LogGen
from Utilities import XLUtilites


class Test002_DDT_Login:
    baseURL = Config.BaseURL()
    path = "D:\\Ecommerence\\TestData\\LoginDatas.xlsx"
    loggers = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.loggers.info("******TestCaseLOGIN002*******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtilites.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel", self.rows)
        list_status = []  # Empty list variable

        for r in range(2, self.rows + 1):
            self.user = XLUtilites.readData(self.path, 'Sheet1', r, 1)  # sheet name rowno and column
            self.password = XLUtilites.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtilites.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.loggers.info("***Passed***")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == 'Fail':
                    self.loggers.info("***Failed***")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***Failed***")
                    self.lp.clickLogout()
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    self.loggers.info("***Passed**")
                    self.lp.clickLogout()
                    list_status.append("Pass")
        if 'Fail' not in list_status:
            self.loggers.info("DDT is passed")
            self.driver.close()
            assert True
        else:
            self.loggers.info("DDT is failed")
            self.driver.close()
            assert False

        self.loggers.info("End of DDT test")
