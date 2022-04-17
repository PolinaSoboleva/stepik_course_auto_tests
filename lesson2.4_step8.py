from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import math

def matfun(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

button=browser.find_element(By.ID,"book")
browser.execute_script("return arguments[0].scrollIntoView(true);",button)
WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
button.click()

x1=browser.find_element_by_id("input_value").text
y=matfun(x1)
browser.find_element_by_id("answer").send_keys(y)
button1=browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);",button1)
button1.click()
