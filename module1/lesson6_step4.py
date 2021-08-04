# Вам нужно открыть страницу по ссылке
# и заполнить форму на этой странице с помощью Selenium.
# Если всё сделано правильно, то вы увидите окно с проверочным кодом.
# Это число вам нужно ввести в качестве ответа в этой задаче.

# Для решения этой задачи есть шаблон кода,
# в который нужно только подставить нужные значения для поиска

from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# Системы UNIX/Linux ожидают пустую строку в конце файла,
# если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться


# Подберите селекторы и запустите из командной строки, так же, как в уроке 2:
# python lesson6_step4.py
# Все последующие задачи с кодом запускайте по аналогии.