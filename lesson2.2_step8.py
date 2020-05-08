import os
import time

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

        # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('.form-group>[name="firstname"]')
    input1.send_keys("some_name")
    input2 = browser.find_element_by_css_selector('.form-group>[name="lastname"]')
    input2.send_keys("lastname")
    input3 = browser.find_element_by_css_selector('.form-group>[name="email"]')
    input3.send_keys("test@email.com")

    #загружаем файл
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, 'f.txt')
    attach = browser.find_element_by_css_selector("#file")
    attach.send_keys(file_path)



    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()