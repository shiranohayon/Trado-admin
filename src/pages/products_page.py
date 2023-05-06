from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.products_locators import ProductsLocators
from time import sleep
import os
from src.utils.db import get_random_product
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver


    def search_bar_keyword(self, input):
        sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.search_field))).send_keys(input)
        sleep(2)

    def get_product_name_to_search(self, db):
        product = get_random_product(db)
        return product.get("name")

    def get_product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.product_name).text

    def click_products_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.products_btn))).click()
        sleep(2)

    def get_no_results_text(self):
        text = self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.no_results_text).text
        return text

    def click_products_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.products_menu).click()

    def click_add_product_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.add_product_btn).click()
        sleep(2)

    def input_product_barcode(self, input):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.barcode_field))).send_keys(input)



    def upload_photo_to_product(self):
        # Find the text field element
        textfield = self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.photo_field)
        image_path = os.path.abspath("C:\\Users\\User\\IMG_1276-1small-1.jpg")
        # Fill in the image path in the text field
        textfield.send_keys(image_path)
        sleep(3)

    def input_product_name(self, input):
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.name_field).send_keys(input)
    def input_product_price(self, input):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.price_field))).send_keys(input)
    def input_product_sale_price(self, input):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.sale_price_field))).send_keys(input)

    def click_product_category(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.product_category))).click()

    def click_category_first_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ProductsLocators.category_first_option))).click()

    def click_store_first_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ProductsLocators.store_first_option))).click()

    def click_next_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.next_btn))).click()

    def click_store_field(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.store_field))).click()


    def click_and_input_unitsincarton(self, input):
       WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.unitsincarton_field))).send_keys(input)

    def is_barcode_error_msg_display(self):
        return self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.barcode_error_msg)

    def get_product_price_from_page(self):
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.third_product_price))).text
        replace_text = text.replace("₪", "")
        replace_text = float(replace_text)
        return replace_text

    def get_barcode_from_page(self):
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.third_product_barcode))).text
        return text

    def get_all_barcodes_from_page(self):
        barcodes = []
        barcode_elements = self.driver.find_elements(By.CSS_SELECTOR, ProductsLocators.all_barcodes_in_page)
        for element in barcode_elements:
            barcodes.append(element.text)
        return barcodes

    def get_product_name_from_page(self):
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.third_product_name))).text
        return text

    def click_edit_product_description(self):
        first_button = WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, ProductsLocators.edit_product_description_btn)))
        action = ActionChains(self.driver)
        action.move_to_element(first_button).perform()
        action.click(first_button).perform()
        sleep(2)

    def delete_text_on_description_popup(self):
       element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.text_on_description_popup)))
       element.clear()


    def input_text_to_description_field(self, input):
       element = self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.text_on_description_popup)
       self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.text_on_description_popup).click()
       self.driver.execute_script("arguments[0].value = arguments[1];", element, input)
       sleep(2)


    def click_save_description_btn(self):
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ProductsLocators.save_description_btn).click()
        sleep(2)

    def click_next_product_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.next_product_page_btn))).click()
        sleep(3)

    def click_on_product_amount_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.product_amount_option_on_page))).click()
        sleep(2)

    def click_on_20_products_on_page_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ProductsLocators.amount_btn_20_products))).click()
        sleep(2)






