from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import os

def create_file():
    with open('auto_tests_course/lesson_2_2/file.txt', 'w') as wrt:
        wrt.write('test write in file')

def get_current_path():
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'file.txt')
    return file_path

try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get('https://suninjuly.github.io/file_input.html')

    first_name = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    first_name.send_keys('test_firstname')

    last_name = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    last_name.send_keys('test_lastname')

    email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys('test_email')

    create_file()

    file_btn = browser.find_element(By.CSS_SELECTOR, '#file')
    file_btn.send_keys(get_current_path())


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(15)
    browser.quit()
