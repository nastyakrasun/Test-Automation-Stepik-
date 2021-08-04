from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/math.html"  # Открыть страницу http://suninjuly.github.io/math.html.
    browser = webdriver.Chrome()
    browser.get(link)
# На странице есть radiobuttons, для которых выбрано значение по умолчанию
    people_radio = browser.find_element_by_id("peopleRule")  # Найдём этот radiobutton с помощью WebDriver

    people_checked = people_radio.get_attribute("checked")  # Найдём атрибут "checked" с помощью встроенного метода get_attribute
    print("value of people radio: ", people_checked)  # проверим значение атрибута
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")  # Найдём radiobutton, для кот не выбрано значение по умолчанию, с помощью WebDriver
    robots_checked = robots_radio.get_attribute("checked")  # Найдём атрибут "checked" с помощью встроенного метода get_attribute
    print("value of robots radio: ", robots_checked)  # проверим значение атрибута
    assert robots_checked is None

# Так же можно проверять наличие атрибута disabled, который определяет, может ли пользователь взаимодействовать с элементом
    button = browser.find_element_by_css_selector("button.btn")  # находим кнопку, для которой установлено disabled
    button_checked = button.get_attribute("disabled")  # проверяем, установлено ли значение
    print("has button atribute disabled?", button_checked)  # принтим значение атрибута
    assert button_checked is None  # значение не установлено

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    # пустая строка в конце для Linux)