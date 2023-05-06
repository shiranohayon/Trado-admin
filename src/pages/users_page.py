from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import src.locators.users_locators as ul
from selenium.webdriver.common.by import By
from src.locators.users_locators import UserLocators
from time import sleep


class Userpage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_users_on_main_menu(self):
        WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.user_main_menu_btn,))).click()

    def click_on_three_dots(self):
        WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.three_dots_left_side,))).click()
        sleep(1)

    def click_add_btn(self):
        WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.add_btn,))).click()
        sleep(1)

    def invalid_email(self):
        first_name= WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_first_name,)))
        first_name.send_keys("עומר")
        last_name = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_last_name,)))
        last_name.send_keys("גל")
        email = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_email,)))
        email.send_keys("o@g..")
        sleep(2)

    def valid_email(self):
        first_name= WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_first_name,)))
        first_name.send_keys("עומר")
        last_name = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_last_name,)))
        last_name.send_keys("גל")
        email = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_email,)))
        email.send_keys("og@gmail.com")
        sleep(2)

    def error_message_email(self):
        message = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.error_message_email,)))
        return message

    def invalid_phone(self):
        first_name= WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_first_name,)))
        first_name.send_keys("עומר")
        last_name = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_last_name,)))
        last_name.send_keys("גל")
        email = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_email,)))
        email.send_keys("grfhfjngn@gmail.com")
        phone = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_phone,)))
        phone.send_keys("01010")
        sleep(2)

    def valid_phone(self):
        first_name= WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_first_name,)))
        first_name.send_keys("עומר")
        last_name = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_last_name,)))
        last_name.send_keys("גל")
        email = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_email,)))
        email.send_keys("og@gmail.com")
        phone = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.input_phone,)))
        phone.send_keys("0571523645")
        sleep(2)

    def error_message_phone(self):
        message = WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.error_message_phone,)))
        return message

    def input_user_search(self, user_name):
        WDW(self.driver, 5).until(EC.visibility_of_element_located((*ul.UserLocators.user_search_bar,))).send_keys(user_name)
        sleep(2)

    def first_search(self):
        WDW(self, 5).until(EC.visibility_of_element_located((*ul.UserLocators.user_search_1st_output,)))

    def search_result(self):
        result = self.driver.find_element(By.XPATH, UserLocators.search_result)
        sleep(2)
        return result
    