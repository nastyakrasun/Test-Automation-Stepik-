from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    # time.sleep(10)  # чтобы тест прошёл без ошибок - но мы не знаем времени появления кнопки!
    button = browser.find_element_by_id("verify")
    # time.sleep(10)  # чтобы тест прошёл без ошибок - но мы не знаем времени появления кнопки!
    button.click()
    # time.sleep(10)  # чтобы тест прошёл без ошибок - но мы не знаем времени появления кнопки!
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
