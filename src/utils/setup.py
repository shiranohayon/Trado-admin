
from src.pages.orders_page import Orderspage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.pages.department_page import Departmentpage
from time import sleep
from src.utils.db import create_mongo_connection
from src.pages.login_page import Loginpage
from src.pages.products_page import ProductsPage
from src.pages.users_page import Userpage


class WebDriverSetup:
    @pytest.fixture()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://qa-admin.trado.co.il/ ')
        self.driver.maximize_window()
        sleep(5)
        self.login_page = Loginpage(self.driver)
        self.login_page.valid_login()
        self.orders_page = Orderspage(self.driver)
        self.department_page = Departmentpage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.db = create_mongo_connection()
        self.user_page = Userpage(self.driver)

        yield self.driver
        self.driver.quit()

    @pytest.fixture()
    def setUp_without_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://qa-admin.trado.co.il/#/login")
        self.driver.maximize_window()
        sleep(3)
        self.login_page = Loginpage(self.driver)

        sleep(3)
        yield self.driver
        self.driver.quit()