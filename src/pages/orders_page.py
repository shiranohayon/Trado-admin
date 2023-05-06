

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.orders_locators import OrdersLocators
from time import sleep
import random
from selenium.webdriver.support.color import Color


class Orderspage:
    def __init__(self, driver):
        self.driver = driver

    def click_order_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.order_btn))).click()
        sleep(3)

    def search_valid(self):
        search = self.driver.find_element(By.XPATH, OrdersLocators.search_input)
        search.send_keys("1242")
        sleep(1)

    def search_invalid(self):
        search = self.driver.find_element(By.XPATH, OrdersLocators.search_input)
        search.send_keys("=====")
        sleep(1)

    #assert result search
    def search_result(self):
        x = self.driver.find_element(By.XPATH, OrdersLocators.search_result)
        sleep(2)
        return x

    def click_english_language_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.english_language_btn))).click()
        sleep(4)


    def click_orders_menu_btn(self):
         WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.orders_menu_btn))).click()
         sleep(1)

         WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.orders_menu_btn))).click()
         sleep(1)

    #assert english_language
    def menu_window_display(self):
        x =WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, OrdersLocators.orders_menu_btn)))
        return x

    def click_order_1242(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.order_1242))).click()
        sleep(1)

    def weight_valid(self):
        search = self.driver.find_element(By.XPATH, OrdersLocators.weight_input)
        search.send_keys("12")
        sleep(1)

    def click_mark_order_as_ready_for_delivery_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.status_btn))).click()
        sleep(2)

    def message_display(self):
        x = self.driver.find_element(By.CLASS_NAME, OrdersLocators.message)
        sleep(2)
        return x

    def click_mark_order_as_sent_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.status_btn))).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.status_btn))).click()
        sleep(2)

    def click_order_has_arrived_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.status_btn))).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.status_btn))).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.status_btn))).click()
        sleep(2)

    def get_first_order_number_from_page(self):
        text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, OrdersLocators.first_order_number))).get_attribute("innerText")
        sleep(2)
        return text





    def click_orders_btn(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.orders_btn))).click()
            sleep(2)

    def txt_received_btn(self):
            title = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.received)))
            return title

    def txt_ready_btn(self):
            title = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.ready)))
            return title

    def txt_on_delivery_btn(self):
            title = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.on_delivery)))
            return title

    def txt_finish_btn(self):
            title = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.finish)))
            return title

    def click_id_order_1236(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.order_id_1236))).click()

    def click_missing_btn(self):
            btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.missing_btn)))
            btn.click()
            sleep(3)
            return btn

    def missing_display(self):
            btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, OrdersLocators.missing_btn)))
            color_rgb = btn.value_of_css_property("color")
            color_hex = Color.from_string(color_rgb).hex
            return color_hex

    def click_quantity(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.quantity))).click()

    def quantity_display(self):
            num = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.quantity))).get_attribute("innerText")
            sleep(3)
            return num

    def click_one_quantity(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,OrdersLocators.one_quantity))).click()
            sleep(3)

    def click_five(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.five))).click()
            sleep(3)

    def click_replace(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.replace))).click()

    def replace_search(self, product):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.replace_search))).send_keys(product)
            sleep(3)
            return product

    def click_lemon(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.lemon))).click()
            sleep(3)

    def lemon_display_(self):
            product = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, OrdersLocators.lemon))).get_attribute("innerText")
            sleep(3)
            return product

    def lemon_display_1(self):
            product = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, OrdersLocators.search_list))).get_attribute("innerText")
            sleep(3)
            return product
    def lemon_name_display(self):
            name = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, OrdersLocators.name_lemon))).is_displayed()
            sleep(3)
            return name

    def search(self, id):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.search))).send_keys(id)
            sleep(3)
            return id

    def click_1168(self):
            btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.order_id_1168)))
            btn.click()
            sleep(3)
            return btn

    def click_address(self):
            btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.address)))
            btn.click()
            sleep(10)
            return btn

    def click_ready_for_delivery(self):
            btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.ready_for_delivery)))
            btn.click()
            return btn

    def weight_alert_display(self):
            alert = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, OrdersLocators.weight_alert))).get_attribute("innerText")
            sleep(3)
            return alert

    def click_surfaces(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.surfaces))).click()

    def click_one_surface(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.one_surface))).click()
            sleep(3)

    def surface_alert_display(self):
            alert = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, OrdersLocators.surface_alert))).get_attribute("innerText")
            sleep(3)
            return alert

    def click_right_btn(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.right_btn))).click()
            sleep(3)

    def click_double_right_btn(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.double_right))).click()
            sleep(3)

    def click_left_btn(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.left_btn))).click()
            sleep(3)

    def click_double_left_btn(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.double_left))).click()
            sleep(3)

    def row_number_view_display(self):
            num = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.row_number_view))).get_attribute("innerText")
            sleep(3)
            return num

    def num_of_product_display(self):
            num = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, OrdersLocators.weight_alert))).is_displayed()
            sleep(3)
            return num

    def click_number(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.how_many_orders))).click()

    def click_100_btn(self):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.btn_100))).click()
            sleep(3)

    def click_random_num(self):
            test = random.randrange(7)
            print(f"test={test}")
            if test == 0:
                element =  WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.btn_20)))

            elif test == 1:
                element =  WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.btn_50)))

            elif test == 2:
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.btn_75)))

            elif test == 3:
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.btn_100)))

            elif test == 4:
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.btn_150)))

            elif test == 5:
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.btn_200)))
            else:
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.all_btn)))

            print(f"element={element}")
            element.click()
            sleep(3)
            return element



    def row_number_view_2_display(self):
            num = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, OrdersLocators.row_number_view_2))).get_attribute("innerText")
            sleep(3)
            return num


