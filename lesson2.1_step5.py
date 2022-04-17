from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link='http://suninjuly.github.io/math.html'
    browser=webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    
    in1=browser.find_element_by_css_selector("#answer")
    in1.send_keys(y)

    contr=browser.find_element_by_css_selector("[for='robotCheckbox']")
    contr.click()

    contr1=browser.find_element_by_css_selector("[for='robotsRule']")
    contr1.click()

    but=browser.find_element_by_css_selector("button.btn")
    but.click()
finally:
    time.sleep(10)
    browser.quit()