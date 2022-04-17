from selenium import webdriver
import math
import time

def matfun(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link=' http://SunInJuly.github.io/execute_script.html'
    browser=webdriver.Chrome()
    browser.get(link)

    xcor=browser.find_element_by_id("input_value").text
    inp=browser.find_element_by_id("answer")
    y=matfun(xcor)
    inp.send_keys(y)
    
    e1=browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);",e1)
    e1.click()
    e2=browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);",e2)
    e2.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);",button)
    button.click()
finally:
    time.sleep(5)
    browser.quit()