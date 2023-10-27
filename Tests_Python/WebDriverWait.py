# Ждем появление текста на сайте, затем обрабатываем его

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    price = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    driver.find_element(By.ID, "book").click()
    x = driver.find_element(By.ID, "input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    driver.find_element(By.ID, "answer").send_keys(y)
    driver.find_element(By.ID, "solve").click()

finally:
    sleep(10)
    driver.quit()
