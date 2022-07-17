from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(12)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.XPATH, '//div[@class = "card-body"]/button').click()

    button = browser.find_element(By.XPATH, '//button[@id = "solve"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.XPATH, '//span[@id = "input_value"]').text))

    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()