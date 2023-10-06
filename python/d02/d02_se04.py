from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://google.com')
#자바 스크립트 호출 할 때 사용
r = driver.execute_script("return 1000*50")
print(r)