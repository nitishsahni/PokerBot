import string
import time
from random import choice

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def get_password():
    password = input("Your password: ")
    if not password:
        return 'GamblingIsB4D'
    return password


def get_number_accounts():
    num = input("Number of accounts needed: ")
    if not num:
        return 1
    return num


def get_email():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = TorBrowserDriver("PATH TO BUNDLE")
    driver.get("https://tempmail.net/")
    email_element = driver.find_element_by_id("eposta_adres")
    email_to_use = email_element.get_attribute('value')
    driver.quit()
    return email_to_use


def get_username(chars=string.ascii_letters + string.digits, length=8):
    return ''.join([choice(chars) for i in range(length)])


def create_account_and_login(email, username, password, num):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://poker.pokerstars.in")
    create_account(email, username, password, driver, num)
    login(username, password, driver)


def create_account(email, username, password, driver, num):
    for i in range(num):
        driver.find_element_by_id("startRegister").click()
        time.sleep(1)
        email_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#psram_createaccount_email")))
        email_input.send_keys(email)
        username_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#psram_createaccount_username")))
        username_input.send_keys(username)
        pwd_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#psram_createaccount_password")))
        pwd_input.send_keys(password)
        time.sleep(2)
        submit_button = driver.find_element_by_xpath("//button[@class='btn btn-success btn-big btn-full-width']")
        submit_button.click()
        el = driver.find_elements_by_xpath("//label[contains(string(), 'Select All')]")[0]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(el, 5, 5)
        action.click()
        action.perform()
        submit_button = driver.find_element_by_xpath("//button[@class='btn btn-success btn-big btn-full-width']")
        time.sleep(3)
        submit_button.click()
        time.sleep(3)
        close_button = driver.find_element_by_xpath("//button[@class='btn previous']")
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(close_button, 5, 5)
        action.click()
        action.perform()


def login(username, password, driver):
    login = driver.find_element_by_id("startLogin")
    login.click()
    time.sleep(1)
    email_input = driver.find_element_by_id("psramusernamepopup")
    email_input.send_keys(username)
    email_input.send_keys(Keys.TAB)
    pwd_input = driver.switch_to.active_element
    pwd_input.send_keys(password)
    time.sleep(1)
    pwd_input.submit()
    time.sleep(10)
    driver.quit()


class Generator:

    def __init__(self):
        password = get_password()
        number_of_accounts = get_number_accounts()
        email = get_email()
        username = get_username()
        create_account_and_login(email, username, password, number_of_accounts)


if __name__ == '__main__':
    Generator()
