import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:
    customer_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    link_customer_menu_items_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    link_add_button_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txt_Email_xpath = "//*[@id='Email']"
    txt_password_xpath = "//*[@id='Password']"
    txt_first_name_xpath = '//*[@id="FirstName"]'
    txt_last_name_xpath = '//*[@id="LastName"]'
    rdMale_gender_id = 'Gender_Male'
    rdFemale_gender_id = 'Gender_Female'
    txt_DOB_xpath = '//*[@id="DateOfBirth"]'
    txt_Company_xpath = '//*[@id="Company"]'
    Admin_content_xpath = '//*[@id="AdminComment"]'
    save_button_xpath = '/html/body/div[3]/div[1]/form/div[1]/div/button[1]'
    drpmgofVendors_xpath = '//*[@id="VendorId"]'

    def __init__(self, driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.customer_menu_xpath).click()

    def clickonCustomerMenuItems(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_items_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element(By.XPATH, self.link_add_button_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_Email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def setfirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_first_name_xpath).send_keys(firstname)

    def setlastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_last_name_xpath).send_keys(lastname)

    def clickonDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(dob)

    def setMangervendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgofVendors_xpath))
        drp.select_by_visible_text(value)

    def setcompanyName(self, cmpname):
        self.driver.find_element(By.XPATH, self.txt_Company_xpath).send_keys(cmpname)

    def setAdmincontent(self, admins):
        self.driver.find_element(By.XPATH, self.Admin_content_xpath).send_keys(admins)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMale_gender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemale_gender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMale_gender_id).click()

    def saveonclick(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
