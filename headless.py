from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#webdriver.Chrome(): Returns us an instance of Chrome driver through which we will be interacting with Chrome browser.
#Options(): Through attributes of this class we can send browser launch parameters. In our case it is options.headless = True which will launch browser without UI(headless).

# instance of Options class allows
# us to configure Headless Chrome
options = Options()

# this parameter tells Chrome that
# it should be run without UI (Headless)
options.headless = True

# initializing webdriver for Chrome with our options
driver = webdriver.Chrome(options=options)

# getting GeekForGeeks webpage
driver.get('https://www.geeksforgeeks.org')

# We can also get some information
# about page in browser.
# So let's output webpage title into
# terminal to be sure that the browser
# is actually running.
print(driver.title)

# close browser after our manipulations
driver.close()