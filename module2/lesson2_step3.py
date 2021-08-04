# Напишите код, который реализует следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"
# Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html.
# Ваш код и для нее тоже должен пройти успешно.

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"  # Открыть страницу http://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("span#num1")
    x = int(x_element.text)
    # print(x)  # проверяла визуально чтобы проставить тип данных
    y_element = browser.find_element_by_css_selector("span#num2")
    y = int(y_element.text)
    # print(y)  # проверяла визуально чтобы проставить тип данных
    result = x + y  # Посчитать сумму заданных чисел
    # print(result)  # проверяла визуально чтобы проставить тип данных

    select = Select(browser.find_element_by_tag_name("select"))  # Выбрать в выпадающем списке значение равное расчитанной сумме
    select.select_by_visible_text(str(result))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Нажать на кнопку Submit.

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # строчка для Linux)