""""Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
"""

import time,math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    wait = WebDriverWait(browser, 12)
    but1 = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    # нажимаем бук
    button1 = browser.find_element_by_css_selector('#book').click()

    # появляетс невдимая ранее часть
    element = wait.until(EC.element_to_be_clickable((By.ID, 'input_value')))
    element_x = browser.find_element_by_css_selector('#input_value')
    x = element_x.text
    y = calc(x)

    input1 = wait.until(EC.element_to_be_clickable((By.ID, 'answer')))
    input1_1 = browser.find_element_by_css_selector('#answer').send_keys(y)
    button = browser.find_element_by_css_selector('#solve').click()


finally:
    time.sleep(7)
    browser.quit()


