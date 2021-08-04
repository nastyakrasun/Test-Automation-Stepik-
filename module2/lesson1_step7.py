# Ваша программа должна выполнить следующие шаги:
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"  # Открыть страницу http://suninjuly.github.io/get_attribute.html.
    browser = webdriver.Chrome()
    browser.get(link)

    image_element = browser.find_element_by_css_selector("img#treasure")  # найти переменную х по css-селектору, у которого айдишник спана равен input_value
    x = image_element.get_attribute("valuex")  # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.

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
