from src.utils.setup import WebDriverSetup
import allure

class TestTORADO(WebDriverSetup):
    @allure.title("test_1_valid_login")
    def test_1_valid_login(self, setUp):
        assert self.driver.current_url == "https://qa-admin.trado.co.il/#/"
        text_hello_user = self.login_page.hello_user().get_attribute("innerText")
        assert text_hello_user == 'שלום slamonnnהתנתק'

    def test_2_invalid_phone(self, setUp_without_login):
        self.login_page.invalid_phone()
        text_error_message = self.login_page.phone_error_message().get_attribute("innerText")
        assert text_error_message == "מס׳ טלפון לא תקין"

    def test_3_invalid_code(self, setUp_without_login):
        self.login_page.invalid_code()
        text_error_message = self.login_page.code_error_message().get_attribute("innerText")
        assert text_error_message == "faild to login undefined"

    def test_4_logout(self ,setUp):
        self.login_page.click_logout_btn()
        assert self.driver.current_url == "https://qa-admin.trado.co.il/#/login"
