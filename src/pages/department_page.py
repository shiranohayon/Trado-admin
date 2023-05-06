from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.locators.department_locators import Xpath_department
from time import sleep
from src.utils.mac_db import get_random_departments



class Departmentpage:
    def __init__(self, driver):
        self.driver = driver

    def department(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.department)))
        return title

    def click_department(self):
        self.department().click()
    def search(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.search)))
        return title

    def click_search(self):
        self.search().click()

    def id(self):
        title = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.id)))
        return title

    def click_id(self):
        self.id().click()

    def name(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.name)))
        return title

    def click_name(self):
        self.name().click()

    def photo(self):
        title = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.photo)))
        return title

    def click_photo(self):
        self.photo().click()
    def coverphoto(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.coverphoto)))
        return title

    def click_coverphoto(self):
        self.coverphoto().click()
    def active(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.active)))
        return title

    def click_active(self):
        self.active().click()

    def date(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.date)))
        return title

    def click_date(self):
        self.date().click()
    def dropdown(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.dropdown)))
        return title

    def click_dropdown(self):
        self.dropdown().click()

    def add(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.add)))
        return title

    def click_add(self):
        self.add().click()

    def fill_new_name(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.fill_new_name)))
        return title

    def add_department(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.add_department)))
        return title

    def click_add_department(self):
        self.add_department().click()


    def first_product_name(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.first_product_name)))
        return title
    def second_name(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.second_name)))
        return title

    def first_id(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.first_id)))
        return title

    def second_id(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.second_id)))
        return title

    def first_image(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.first_image)))
        return title

    def first_coverimage(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.first_coverimage)))
        return title

    def first_active(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.first_active)))
        return title

    def first_date(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.first_date)))
        return title

    def second_date(self):
        title = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, Xpath_department.second_date)))
        return title

    def get_department_name_to_search(self, db):
        department = get_random_departments(db)
        return department.get("name")
