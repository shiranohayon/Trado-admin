import allure
from src.utils.setup import WebDriverSetup
# Convert the date strings into datetime objects for comparison
from datetime import datetime
from faker import Faker
from time import sleep
import allure


class TestTORADO(WebDriverSetup):

    # @allure.title("test_1_search_valid")
    def test_1_search_valid(self, setUp):
        self.department_page.click_department()
        self.department_page.search().send_keys('arad')
        result = self.department_page.first_product_name()
        assert result.text == 'arad'

    def test_2_order_by_id_is_valid(self, setUp):
        self.department_page.click_department()
        self.department_page.click_id()
        result = self.department_page.first_id()
        ref = self.department_page.second_id()
        assert result.text < ref.text, "text1 is greater than text2"

    def test_3_order_by_name_is_valid(self, setUp):
        self.department_page.click_department()
        self.department_page.click_name()
        sleep(3)
        result = self.department_page.first_product_name()
        ref = self.department_page.second_name()
        assert result.text < ref.text, "text1 is greater than text2"

    def test_4_order_by_image_is_valid(self, setUp):
        self.department_page.click_department()
        self.department_page.click_photo()
        element_with_image = self.department_page.first_image()
        # Assert that the element has an image attached
        assert element_with_image.find_element_by_tag_name("img"), "Element does not have an image attached"
        # Click on the element to order by it
        self.department_page.click_photo()
        ordered_element = self.department_page.first_image()
        # Assert that the element no longer has an image attached
        assert not ordered_element.find_element_by_tag_name("img"), "Element still has an image attached after ordering"

    def test_5_order_by_coverimage_is_valid(self, setUp):
        self.department_page.click_department()
        self.department_page.click_photo()
        element_with_image = self.department_page.first_coverimage()
        # Assert that the element has an image attached
        assert element_with_image.find_element_by_tag_name("img"), "Element does not have an image attached"
        # Click on the element to order by it
        self.department_page.click_photo()
        ordered_element = self.department_page.first_coverimage()
        # Assert that the element no longer has an image attached
        assert not ordered_element.find_element_by_tag_name("img"), "Element still has an image attached after ordering"

    def test_6_order_by_active_is_valid(self, setUp):
        self.department_page.click_department()
        self.department_page.click_active()
        sleep(2)
        self.department_page.click_department()
        order_by_element = self.department_page.first_active()
        assert "✓" not in order_by_element.text

    def test_7_order_by_created_at_is_valid(self, setUp):
        self.department_page.click_department()
        self.department_page.click_date()
        # Get the text content of the date elements
        first_date = self.department_page.first_date().text
        second_date = self.department_page.second_date().text
        first_date_obj = datetime.strptime(first_date, '%d/%m/%y, %H:%M')
        second_date_obj = datetime.strptime(second_date, '%d/%m/%y, %H:%M')
        # Assert that the first date is more recent than the second date
        assert first_date_obj < second_date_obj, "The first date is more recent than the second date."

    def test_10_add_new_department(self, setUp):
        self.department_page.click_department()
        self.department_page.click_dropdown()
        self.department_page.click_add()
        fake = Faker()
        random_name = fake.name()
        self.department_page.fill_new_name().send_keys(random_name)
        self.department_page.click_add_department()
        self.department_page.search().send_keys(random_name)
        sleep(10)
        result = self.department_page.first_product_name()
        assert result.text == random_name


    #for future project - a db test
    #
    # def test_search_valid_department_display_first(self, setUp):
    #     self.department_page.click_department()
    #     department_name_in_db = self.department_page.get_department_name_to_search(self.db)
    #     self.department_page.search.send_keys(department_name_in_db)
    #     department_name_on_page = self.department_page.name().text
    #     assert department_name_in_db == department_name_on_page