import time

import allure
from src.utils.setup import WebDriverSetup
import src.locators.users_locators as ul


class TestUsers(WebDriverSetup):

    def test_invalid_email(self, setUp):
        self.user_page.click_on_users_on_main_menu()
        self.user_page.click_on_three_dots()
        self.user_page.click_add_btn()
        self.user_page.invalid_email()
        error_message = self.user_page.error_message_email().get_attribute("innerText")
        assert error_message == "דוא״ל לא תקין"

    def test_invalid_phone(self, setUp):
        self.user_page.click_on_users_on_main_menu()
        self.user_page.click_on_three_dots()
        self.user_page.click_add_btn()
        self.user_page.invalid_phone()
        error_message = self.user_page.error_message_phone().get_attribute("innerText")
        assert error_message == "מס׳ טלפון לא תקין"

    def test_invalid_search(self ,setUp):
        self.user_page.click_on_users_on_main_menu()
        self.user_page.input_user_search("======")
        time.sleep(2)
        text_search_result = self.user_page.search_result().get_attribute("innerText")
        assert text_search_result == "סה״כ: 0 שורות"

    def test_search_bar_for_users(self, setUp):
        self.user_page.click_on_users_on_main_menu()
        self.user_page.input_user_search("ביבי")
        time.sleep(3)
        assert "ביבי" in self.driver.find_element(*ul.UserLocators.user_search_1st_output,).text

    def test_invalid_search_bar_for_users(self, setUp):
        self.user_page.click_on_users_on_main_menu()
        self.user_page.input_user_search("1asd16a1d5ss")
        time.sleep(3)
        assert "15s5sad6" not in self.driver.find_element(*ul.UserLocators.user_search_1st_output,).text

    def test_valid_email(self, setUp):
        self.user_page.click_on_users_on_main_menu()
        self.user_page.click_on_three_dots()
        self.user_page.click_add_btn()
        self.user_page.valid_email()
        assert self.driver.current_url == "https://qa-admin.trado.co.il/#/users"

    def test_valid_phone(self, setUp):
        self.user_page.click_on_users_on_main_menu()
        self.user_page.click_on_three_dots()
        self.user_page.click_add_btn()
        self.user_page.valid_phone()
        assert self.driver.current_url == "https://qa-admin.trado.co.il/#/users"

