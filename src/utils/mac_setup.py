from src.pages.orders_page import Orderspage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.pages.login_page import Loginpage
from src.pages.department_page import Departmentpage
from time import sleep
from src.utils import mac_db
from src.pages.login_page import Loginpage
from src.pages.products_page import ProductsPage
from src.utils.mac_db import create_mongo_connection


class WebDriverSetup:
    @pytest.fixture()
    def setUp(self):
        service = Service(executable_path=chromedriver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get('https://qa-admin.trado.co.il/ ')
        self.driver.maximize_window()
        sleep(5)
        self.login_page = Loginpage(self.driver)
        self.mac_db = create_mongo_connection(mac_db.user_name, mac_db.encoded_password,
                                                 mac_db.db_name, mac_db.ca_cert_file_path)

        self.login_page.valid_login()
        self.orders_page = Orderspage(self.driver)
        self.department_page = Departmentpage(self.driver)
        self.products_page = ProductsPage(self.driver)

        self.department_page = Departmentpage(self.driver)
        self.products_page = ProductsPage(self.driver)

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