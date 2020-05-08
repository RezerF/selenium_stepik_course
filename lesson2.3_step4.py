import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    but1 = browser.find_element_by_css_selector('button.btn')
    but1.click()

    conf = browser.switch_to.alert
    conf.accept()

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    input2 = browser.find_element_by_css_selector("#answer")
    input2.send_keys(y)

    but2 = browser.find_element_by_css_selector("button.btn")
    but2.click()



finally:
    time.sleep(7)
    browser.quit()