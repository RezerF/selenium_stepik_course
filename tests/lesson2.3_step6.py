""""
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""

import os,math,time

from selenium import webdriver

def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('button[type="submit"]').click()

    #переходим на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    button2 = browser.find_element_by_css_selector('button.btn').click()


finally:
    time.sleep(4)
    browser.quit()


