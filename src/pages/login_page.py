from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.login_locators import LoginLocators
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Loginpage:
    def __init__(self, driver):
        self.driver = driver

    def valid_login(self):
        phone = self.driver.find_element(By.XPATH, LoginLocators.phone_number)
        phone.send_keys("1950000000")
        sleep(1)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, LoginLocators.connection_btn))).click()
        sleep(1)
        code = self.driver.find_element(By.XPATH, LoginLocators.code_number)
        code.send_keys("1234")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, LoginLocators.connection_btn))).click()
        sleep(1)

    def hello_user(self):
        x = self.driver.find_element(By.CLASS_NAME, LoginLocators.hello_user)
        sleep(2)
        return x

    def invalid_phone(self):
        phone = self.driver.find_element(By.XPATH, LoginLocators.phone_number)
        phone.send_keys("195")
        sleep(1)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, LoginLocators.connection_btn))).click()
        sleep(1)

    #assert invalid_phone
    def phone_error_message(self):
        error_message = self.driver.find_element(By.CLASS_NAME, LoginLocators.phone_error_message)
        return error_message

    def invalid_code(self):
        phone = self.driver.find_element(By.XPATH, LoginLocators.phone_number)
        phone.send_keys("1950000000")
        sleep(1)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, LoginLocators.connection_btn))).click()
        sleep(1)
        code = self.driver.find_element(By.XPATH, LoginLocators.code_number)
        code.send_keys("@")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, LoginLocators.connection_btn))).click()
        sleep(1)

    #assert invalid_phone
    def code_error_message(self):
        error_message = self.driver.find_element(By.CLASS_NAME, LoginLocators.code_error_message)
        return error_message

    def click_logout_btn(self):
        element = self.driver.find_element(By.XPATH, LoginLocators.logout_btn)
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()
        sleep(2)

