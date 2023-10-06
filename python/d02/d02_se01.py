from selenium import webdriver as wd
from selenium.webdriver.common.by import By

driver = wd.Chrome()
driver.get('https://naver.com')

driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.CLASS_NAME, 'btn_search').click()