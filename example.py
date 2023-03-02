"""import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://admin-demo.nopcommerce.com/')
driver.maximize_window()

textbox_username_id="Email"
textbox_password_id="Password"
button_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
link_customer_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
link_customer_menu_items_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
driver.find_element(By.ID, textbox_username_id).clear()
driver.find_element(By.ID,textbox_username_id).send_keys('admin@yourstore.com')
time.sleep(3)
driver.find_element(By.ID,textbox_password_id).clear()
driver.find_element(By.ID,textbox_password_id).send_keys('admin')
time.sleep(3)
driver.find_element(By.XPATH,button_login_xpath).click()
driver.find_element(By.XPATH,link_customer_menu_xpath).click()
time.sleep(1)
driver.find_element(By.XPATH,link_customer_menu_items_xpath).click()
time.sleep(3)
link_add_button_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
driver.find_element(By.XPATH,link_add_button_xpath).click()
time.sleep(3)
customer_roles_xpath='/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]'
driver.find_element(By.XPATH,customer_roles_xpath).click()
lstadmin='/html[1]/body[1]/div[6]/div[1]/div[2]/ul[1]/li[3]'
driver.find_element(By.XPATH,lstadmin).click()
time.sleep(5)


driver.close()





link_customer_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
link_customer_menu_items_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
link_add_button_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
customer_roles_xpath='/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[5]/div[2]/div/div/input'

driver.find_element(By.XPATH,link_customer_menu_items_xpath).click()
driver.find_element(By.XPATH,link_add_button_xpath).click()
driver.find_element(By.XPATH,customer_roles_xpath).click()

driver.find_element(By.ID,'')
driver.find_element(By.XPATH,'')
driver.find_element(By.LINK_TEXT,'')
driver.find_element(By.NAME,'')
driver.find_element(By.CLASS_NAME,'')
driver.find_element(By.CSS_SELECTOR,'')
driver.find_element(By.PARTIAL_LINK_TEXT,'').send_keys()
import openpyxl
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "www.geeksforgeeks.org"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)
# Give the location of the file
path = "D:\\LoginData1.xlsx"

# workbook object is created
wb_obj = openpyxl.load_workbook(path)


sheet_obj = wb_obj.active

max_col = sheet_obj.max_column

# Will print a particular row value
for i in range(1, max_col + 1):
    cell_obj = sheet_obj.cell(row = 2, column = i)
    print(cell_obj.value, end = " ")


import segno

video = segno.make('https://docs.google.com/document/d/1Yp5JJ_m13-DImKVHqNmBqFNM0mvANIxM/edit?usp=drivesdk&ouid=106364327883687003401&rtpof=true&sd=true')
video.save('Video.png')"""

"""import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1][0])
print(np.max(arr))
print(arr.dtype)
print(arr.shape)
print(arr.size)
print(arr.repeat(5))
for x in arr:
    print(x)"""
l=list("1234")
l[0]=l[1]=5
print(l)
num= tuple("3234")
for i in num:
    print(i)