from selenium import webdriver
import time
import os
try:
    link='http://suninjuly.github.io/file_input.html'
    browser=webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Polina")
    browser.find_element_by_name("lastname").send_keys("Sobol")
    browser.find_element_by_name("email").send_keys("Sobol@mail.ru")

    current_dir=os.path.abspath(os.path.dirname(__file__))
    file_path=os.path.join(current_dir,'file.txt')
    browser.find_element_by_css_selector("[type='file']").send_keys(file_path)

    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.quit()

