# Вам потребуется написать код, чтобы:
#
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"  # Открыть страницу http://SunInJuly.github.io/execute_script.html.
    browser.get(link)
    x_element = browser.find_element_by_css_selector(
        "span#input_value")  # Считать значение для переменной x.
    x = x_element.text  # Считать значение для переменной x
    y = calc(x)  # Посчитать математическую функцию от x (код для этого приведён выше).

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)  # Ввести ответ в текстовое поле.
    option1 = browser.find_element_by_css_selector("input#robotCheckbox")  # Отметить checkbox "I'm the robot".
    option1.click()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Проскроллить страницу вниз.
    option2 = browser.find_element_by_css_selector("input#robotsRule")  # Выбрать radiobutton "Robots rule!".
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Нажать на кнопку Submit.

finally:
    time.sleep(10)
    browser.quit()
