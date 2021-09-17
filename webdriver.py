
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# driver = webdriver.Firefox()
# should have geckodriver.exe in same dir or give a path to geckodriver.exe in args
options = Options()
options.headless = True
service_args = []
driver = webdriver.Firefox(options=options)
driver.get('http://icanhazip.com')
print(driver.page_source)
driver.close()