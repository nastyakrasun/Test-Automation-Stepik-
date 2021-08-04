# после нажатия кнопки страница откроется в новой вкладке,
# нужно переключить WebDriver на новую вкладку и решить в ней задачу.
#
# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"  # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Нажать на кнопку

    first_window = browser.window_handles[0]  # запомнить имя первой вкладки
    new_window = browser.window_handles[1]  # имя второй вкладки
    print(new_window)

    browser.switch_to.window(new_window)  # переключаемся для работы с новой вкладкой
    # решить там задачу (из предыд уроков тянется)
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
