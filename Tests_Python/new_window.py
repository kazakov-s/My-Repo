# Обработка открытия новой вкладки

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))
    )
    sleep(2) # Пауза для визуализации
    driver.find_element(By.TAG_NAME, "button").click()
    driver.switch_to.window(driver.window_handles[1])
    x = driver.find_element(By.ID, "input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    driver.find_element(By.ID, "answer").send_keys(y)
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    sleep(10)
    driver.quit()
