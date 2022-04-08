from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

serv = Service('./chromedriver')
driver = webdriver.Chrome(service=serv)
url = 'https://cb.am'
driver.get(url)

print(driver.find_element_by_tag_name('thead').text)

driver.find_element_by_class_name('collapse-toggle-btn').click()

print(driver.find_element_by_class_name('blue_td').text)

driver.find_element_by_tag_name('html').send_keys(Keys.END)
