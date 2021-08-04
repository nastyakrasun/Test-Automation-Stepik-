# написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Нажать на кнопку

    confirm = browser.switch_to.alert
    confirm.accept()  # Принять confirm
    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element_by_css_selector(
        "span#input_value")  # найти переменную х по css-селектору, у которого айдишник спана равен input_value
    x = x_element.text  # Считать значение для переменной x
    y = calc(x)  # получила число с ответом

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)  # вставила ответ в текстовое поле.

    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Нажать на кнопку submit

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()