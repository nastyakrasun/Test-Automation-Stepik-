# Ваша программа должна выполнить следующие шаги:
#
# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"  # Открыть страницу http://suninjuly.github.io/math.html.
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("span#input_value")  # найти переменную х по css-селектору, у которого айдишник спана равен input_value
    x = x_element.text  # Считать значение для переменной x
    y = calc(x)  # Посчитать математическую функцию от x (код для этого приведён выше).

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(y)  # Ввести ответ в текстовое поле.

    option1 = browser.find_element_by_css_selector("input#robotCheckbox")  # Отметить checkbox "I'm the robot".
    option1.click()

    option2 = browser.find_element_by_css_selector("input#robotsRule")  # Выбрать radiobutton "Robots rule!".
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Нажать на кнопку Submit.

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
