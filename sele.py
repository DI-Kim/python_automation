# 오래된 자료라 셀레니움은 따로 공부하는 게 좋을 듯

from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()
webdriver.get("https://automatetheboringstuff.com")

elem = webdriver.find_element(
    By.CSS_SELECTOR, "body > div > main > div > ul:nth-child(28) > li:nth-child(1)")
print(elem.text)
