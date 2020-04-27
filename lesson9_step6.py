from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    submit_btn =  browser.find_element_by_css_selector('[type = "submit"]')
    submit_btn.click()

    second_w = browser.window_handles[1]
    browser.switch_to.window(second_w)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    answer = browser.find_element_by_id('answer').send_keys(y)
    submit_btn1 = browser.find_element_by_css_selector('[type = "submit"]')
    submit_btn1.click()
finally:
    time.sleep(30)
    browser.quit()