# Задание
# На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:
#
# Добавьте в самый верх своего кода import math
# Добавьте команду в код, которая откроет страницу: http://suninjuly.github.io/find_link_text
# Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
# str(math.ceil(math.pow(math.pi, math.e)*10000))
# (можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде)
#
# Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
#
# Заполните скриптом форму так же как вы делали в предыдущем шаге урока
#
# После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание

import math  # Добавьте в самый верх своего кода import math
import time

from selenium import webdriver

print(str(math.ceil(math.pow(math.pi, math.e)*10000)))  # Текст ссылки, который нужно найти, зашифрован формулой: расшифровываем принтом

link1 = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    link = browser.find_element_by_link_text("224592") # Добавьте команду, которая найдет ссылку с текстом.
    link.click() # Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
    # Заполните скриптом форму так же как вы делали в предыдущем шаге урока
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