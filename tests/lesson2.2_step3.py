import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select



def calculata_me(a,b):
  return (a + b)


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_elem = browser.find_element_by_css_selector("#num1")
    x = int(first_elem.text)

    #action_elem = browser.find_element_by_css_selector("h2 span:nth-child(3)")
    #d = action_elem.text

    second_elem = browser.find_element_by_css_selector("#num2")
    y = int(second_elem.text)

    s = str(calculata_me(x, y))

    # Ваш код, который заполняет обязательные поля
    my_select = Select(browser.find_element_by_css_selector("#dropdown"))
    my_select.select_by_value(s)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


