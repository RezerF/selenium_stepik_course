import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    input2 = browser.find_element_by_css_selector("#robotCheckbox")
    input2.click()
    input3 = browser.find_element_by_css_selector("#robotsRule")
    input3.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()