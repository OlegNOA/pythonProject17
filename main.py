from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Инициализация драйвера браузера
    browser = webdriver.Chrome()

    # Открытие страницы
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # Считывание значения x
    x_value = browser.find_element_by_id("input_value").text

    # Вычисление значения функции от x
    result = calc(x_value)

    # Прокрутка страницы вниз
    browser.execute_script("window.scrollBy(0, 100);")

    # Ввод ответа в текстовое поле
    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(result)

    # Выбор checkbox "I'm the robot"
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    # Прокрутка страницы вниз, чтобы радиобаттон был виден
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_id("robotsRule"))

    # Выбор радиобаттона "Robots rule!"
    robots_rule_radiobutton = browser.find_element_by_id("robotsRule")
    robots_rule_radiobutton.click()

    # Нажатие на кнопку "Submit"
    submit_button = browser.find_element_by_css_selector("[type='submit']")
    submit_button.click()

    # Получение результата
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    # Закрытие браузера
    browser.quit()
