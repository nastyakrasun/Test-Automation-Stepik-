# Вам дана страница с формой регистрации.
# 	Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля,
# 	отмеченные символом *: First name, last name, email.
# 	Текст для полей может быть любым.
# 	Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!"
# 	с текстом на странице, которая открывается после регистрации.
# 	Для сравнения воспользуемся стандартной конструкцией assert из языка Python.

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # сначала заполняла циклом - нет ошибки во втором случае
    # elements = browser.find_elements_by_xpath("//div[@class='first_block']//input")
    # for element in elements:
    #     element.send_keys("yes")
    # нужно было заполнять код по уникальному css-селектору
    input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
    input3.send_keys("vanya@stepik.com")
    time.sleep(3)
    # чьё-то решение через xpath, уникальные селекторы, не понимаю, почему @required='' указано
    # driver.find_element_by_xpath("//input[contains(@class, 'first') and @required='']").send_keys('first')
    # driver.find_element_by_xpath("//input[contains(@class, 'second') and @required='']").send_keys('second')
    # driver.find_element_by_xpath("//input[contains(@class, 'third') and @required='']").send_keys('third')
    # моё решение было
    # input1 = browser.find_element_by_xpath("//input[contains(@class, 'form-control first')]")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element_by_xpath("//input[contains(@class, 'form-control second')]")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element_by_xpath("//input[contains(@class, 'form-control third')]")
    # input3.send_keys("vanya@stepic.com")
    # ещё чьё-то решение, тоже с уник селекторами
    # first_name_input = browser.find_element_by_css_selector("div.first_block>div.first_class>input.first");
    # first_name_input.send_keys("SomeFirstName");
    # ... аналогично для ост полей

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# оставляем пустую строку
# так как Linux может не выполнить то, что написано на последней строке