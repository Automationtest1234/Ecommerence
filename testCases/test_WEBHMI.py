import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
# Get the Webdriver instance
driver: WebDriver=webdriver.Chrome()
# Get the URL of the webpage
driver.get("http://172.20.153.82/#/")
driver.maximize_window()
driver.save_screenshot("D:\Ecommerence\Screenshots/Homescreen.png")

#Get the username from the user
UserName=driver.find_element(By.XPATH,'//input[@id="input-10"]')
UserName.send_keys("esab")
driver.save_screenshot("D:\Ecommerence\Screenshots/Username.png")

#Get the password from the user
Password=driver.find_element(By.XPATH,'//input[@id="input-13"]')
Password.send_keys("esab")
driver.save_screenshot("D:\Ecommerence\Screenshots/Password.png")

# Login button
driver.find_element(By.XPATH,'//button[@class="base-button base-button--primary base-button--fullwidth"]').click()
time.sleep(2)

# Weld parameters
driver.find_element(By.XPATH,"//div[contains(text(),'Weld parameters')]").click()
time.sleep(1)
driver.save_screenshot("D:\Ecommerence\Screenshots/Weld_parameteres.png")
"""driver.find_element(By.XPATH,"//span[normalize-space()='Fe MCW']").click()
driver.find_element(By.XPATH,"//div[normalize-space()='Fe']").click()
#driver.find_element(By.XPATH,"//input[@id='input-58']").click()
driver.find_element(By.XPATH,"//div[@class='slider-bottom__button slider-bottom__button--inc']").click()
driver.find_element(By.XPATH,"//div[@class='close-button']").click()
time.sleep(1)"""

#Wire material
"""driver.find_element(By.XPATH,"//span[normalize-space()='Fe']").click()
time.sleep(2)"""
#driver.find_element(By.XPATH,"//div[contains(text(),'Fe MCW')]").click()
#time.sleep(2)

# Jobs
driver.find_element(By.XPATH,"//div[contains(text(),'Jobs')]").click()
time.sleep(2)
driver.save_screenshot("D:\Ecommerence\Screenshots/Jobs.png")
#driver.find_element(By.XPATH,"//div[@class='job_title'][normalize-space()='one']").clear()
driver.find_element(By.XPATH,"//div[@class='job_title'][normalize-space()='one']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='activate-button']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='v-image v-responsive header__icon-back theme--light']//div[@class='v-responsive__content']").click()
time.sleep(2)

# Tools
driver.find_element(By.XPATH,"//div[contains(text(),'Tools')]").click()
time.sleep(2)
driver.save_screenshot("D:\Ecommerence\Screenshots/Tools.png")

#Error log
driver.find_element(By.XPATH,"//div[contains(text(),'Error log')]").click()
time.sleep(2)
driver.save_screenshot("D:\Ecommerence\Screenshots/Error_log.png")
driver.find_element(By.XPATH,"//div[@class='v-image v-responsive header__icon-back theme--light']//div[@class='v-responsive__content']").click()
time.sleep(1)

#Truearc compensate
driver.find_element(By.XPATH,"//div[contains(text(),'TRUEARC Compensate')]").click()
time.sleep(2)
driver.save_screenshot("D:\Ecommerence\Screenshots/Turearc.png")
driver.find_element(By.XPATH,"//div[@class='v-image v-responsive header__icon-back theme--light']//div[@class='v-responsive__content']").click()
time.sleep(2)

# Settings
driver.find_element(By.XPATH,"//div[contains(text(),'Settings')]").click()
time.sleep(2)
driver.save_screenshot("D:\Ecommerence\Screenshots/Settings.png")

#Collision Detection
driver.find_element(By.XPATH,"//label[@class='label'][normalize-space()='Active LOW']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//label[@class='label'][normalize-space()='Active HIGH']").click()
time.sleep(2)

#Touch sense
driver.find_element(By.XPATH,"//label[@class='label'][normalize-space()='Active LOW']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[5]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//label[1]").click()
time.sleep(1)

#wire inching speed
n=eval(input("Enter the N value"))
#elements=driver.find_element(By.XPATH,"//div[6]//div[1]//div[1]//div[1]//div[2]").click()
for i in range(n):
    # iteration of wire_inching speed
    driver.find_element(By.XPATH, "//div[6]//div[1]//div[1]//div[1]//div[2]").click()
    driver.find_element(By.XPATH, "//div[@class='slider-bottom__button slider-bottom__button--inc']").click()
    driver.find_element(By.XPATH, "//div [contains(text(),'Done')]").click()
time.sleep(1)

#Torch remote button A
driver.find_element(By.XPATH,"//div[@class='v-select__selection v-select__selection--comma'][normalize-space()='Wire inching forward']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(text(),'Wire inching reverse')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='v-select__selection v-select__selection--comma'][normalize-space()='Wire inching reverse']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(text(),'Gas purge')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='v-select__selection v-select__selection--comma'][normalize-space()='Gas purge']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(text(),'Generic output - 1')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='v-select__selection v-select__selection--comma'][normalize-space()='Generic output - 1']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(text(),'Generic output - 2')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='v-select__selection v-select__selection--comma'][normalize-space()='Generic output - 2']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(text(),'Generic output - 3')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='v-select__selection v-select__selection--comma'][normalize-space()='Generic output - 3']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[contains(text(),'No function')]").click()
driver.find_element(By.XPATH,"//div[@class='v-select__selection v-select__selection--comma'][normalize-space()='No function']").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Wire inching forward')]").click()

#Water cooling
driver.find_element(By.XPATH,"//label[normalize-space()='Forced']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//label[normalize-space()='Auto']").click()
time.sleep(1)

#Theme
driver.find_element(By.XPATH,"//label[normalize-space()='Dark']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//label[normalize-space()='Light']").click()
time.sleep(1)

#About
driver.find_element(By.XPATH,"//span[normalize-space()='About']").click()
time.sleep(1)
driver.save_screenshot("D:\Ecommerence\Screenshots/About.png")
driver.find_element(By.XPATH,"//div[@class='v-image v-responsive header__icon-back theme--light']//div[@class='v-responsive__content']").click()
time.sleep(1)

#Logout
driver.find_element(By.XPATH,"//div[@role='button']//div[@class='v-responsive__content']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[contains(text(),'Log Out')]").click()
time.sleep(2)




