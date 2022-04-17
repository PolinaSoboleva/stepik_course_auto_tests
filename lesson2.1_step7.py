from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link='http://suninjuly.github.io/get_attribute.html'
    browser=webdriver.Chrome()
    browser.get(link)

    pct=browser.find_element_by_id("treasure")
    num=pct.get_attribute("valuex")
    y=calc(num)

    in1=browser.find_element_by_css_selector("#answer")
    in1.send_keys(y)

    contr=browser.find_element_by_id("robotCheckbox")
    contr.click()

    contr1=browser.find_element_by_id("robotsRule")
    contr1.click()

    but=browser.find_element_by_css_selector("button.btn")
    but.click()
finally:
    time.sleep(10)
    browser.quit()