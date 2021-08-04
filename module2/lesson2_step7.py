# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

import os
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # заполнить поля формы циклом (всё равно, что вводим)
    elements = browser.find_elements_by_xpath("//div[@class='form-group']//input")
    for element in elements:
        element.send_keys("yes")  # форма заполнена
    # работаем с загрузкой файла
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # print(current_dir)  # выводит путь до директории - наглядность
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)   # добавляем к этому пути имя файла
    # print(file_path)  # выводит путь до файла - наглядность
    element = browser.find_element_by_css_selector("input#file")
    element.send_keys(file_path)  # файл прикрепили
    # нажимаем на кнопку submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()  # Нажать на кнопку Submit.

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
