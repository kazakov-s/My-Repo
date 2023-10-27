from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get("https://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = int(browser.find_element(By.ID, 'input_value').text)
    x_element = calc(x_element)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(x_element))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()