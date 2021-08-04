# нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")  # Открыть страницу http://suninjuly.github.io/explicit_wait2.html

    browser.execute_script("window.scrollTo(0, 500)") # Проскроллить страницу вниз.

    element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button1 = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, "book")))
    button1.click()

    # browser.implicitly_wait(1)

    # browser.execute_script("window.scrollTo(0, 500)")

    x_element = browser.find_element_by_css_selector(
        "span#input_value")  # найти переменную х по css-селектору, у которого айдишник спана равен input_value
    x = x_element.text  # Считать значение для переменной x
    y = calc(x)  # получила число с ответом

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)  # вставила ответ в текстовое поле.

    button2 = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, "solve")))
    button2.click()  # Нажать на кнопку submit


finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
