from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # создали объект (браузер)
driver.get("https://www.saucedemo.com/")

text_field_username = driver.find_element(By.CSS_SELECTOR, '#user-name')
text_field_password = driver.find_element(By.CSS_SELECTOR, '#password')
button_submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

if text_field_username is None and text_field_password is None and button_submit is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')