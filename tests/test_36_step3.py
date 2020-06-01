import time, math, pytest
from selenium import webdriver

def func_answ():
    return str(math.log(int(time.time())))


@pytest.fixture()
def browser():
    br = webdriver.Chrome() # инициализация браузера
    br.implicitly_wait(5) # выставление неявного ожидания
    yield br  # treatdown код будет выполнятся по завершении
    br.quit()


hide_string = ""


@pytest.mark.parametrize('link',[
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'
])
def test_get_feedback(browser, link): # в качестве аргумента передаем функцию фикстуры и параметр для перебора
    browser.get(link)
    input1 = browser.find_element_by_css_selector('textarea[placeholder="Напишите ваш ответ здесь..."]')
    y = func_answ()
    input1.send_keys(y)
    time.sleep(2)
    button = browser.find_element_by_css_selector('button.submit-submission').click()
    asser = browser.find_element_by_css_selector('pre.smart-hints__hint') # возвращает абракадабру чтобы переветси в текст используем метод текст
    global hide_string
    if asser.text != 'Correct!':
        hide_string += asser.text
    print(hide_string)
    assert asser.text == 'Correct!', f'Test failed for {link}'
