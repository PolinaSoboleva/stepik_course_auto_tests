from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link='http://suninjuly.github.io/selects1.html'
    browser=webdriver.Chrome()
    browser.get(link)

    summ=int(browser.find_element_by_id("num1").text)+int(browser.find_element_by_id("num2").text)
    select=Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(summ))
    browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(10)
    browser.quit()