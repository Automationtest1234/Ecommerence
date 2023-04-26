from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
import pytest
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@allure.severity(allure.severity_level.NORMAL)  # decorators class level
class TestNOP():
    @allure.severity(allure.severity_level.BLOCKER)  # decorator method level
    def test_login(self):
        serv_object = Service("C://Users//Reka//Drivers//chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_object)
        self.driver.implicitly_wait(5)
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.find_element(By.XPATH, "//input[@id='Email']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")
        self.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admi")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:

            # capture screenshot and part of allure report
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_productlist(self):
        pytest.skip("skipping test later it will be implemented")

    @allure.severity(allure.severity_level.MINOR)
    def test_dashboardpage(self):
        serv_object = Service("C://Users//Reka//Drivers//chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_object)
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.find_element(By.XPATH, "//input[@id='Email']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")
        self.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
        status = self.driver.find_element(By.XPATH, "//img[@class='brand-image-xl logo-xl']").is_displayed()
        if status == True:
            assert True  # pytest assertion
        else:
            assert False
        self.driver.close()