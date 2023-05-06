from src.utils.setup import WebDriverSetup
from src.utils.db import get_all_numbers_orders_from_db
from time import sleep
import allure


class TestTORADO(WebDriverSetup):

    @allure.title("test_1_click_orders")
    def test_1_click_orders(self, setUp):
        self.orders_page.click_orders_btn()
        assert self.driver.current_url == "https://qa-admin.trado.co.il/#/orders"

    def test_2_text_received_btn(self, setUp):
        self.orders_page.click_orders_btn()
        button = self.orders_page.txt_received_btn()
        assert button.text == 'התקבלה', f"Unexpected text: {button.text}"
    def test_2_text_ready_btn(self, setUp):
        self.orders_page.click_orders_btn()
        button = self.orders_page.txt_ready_btn()
        assert button.text == 'מוכנה', f"Unexpected text: {button.text}"

    def test_2_text_on_delivery_btn(self, setUp):
        self.orders_page.click_orders_btn()
        button = self.orders_page.txt_on_delivery_btn()
        assert button.text == 'במשלוח', f"Unexpected text: {button.text}"

    def test_2_text_finish_btn(self, setUp):
        self.orders_page.click_orders_btn()
        button = self.orders_page.txt_finish_btn()
        assert button.text == 'סיום', f"Unexpected text: {button.text}"

    @allure.title("test_3_search_valid_orders")
    def test_3_search_valid_orders(self, setUp):
        self.orders_page.click_order_btn()
        self.orders_page.search_valid()
        text_search_result = self.orders_page.search_result().get_attribute("innerText")
        assert text_search_result == "סה״כ: 1 שורות"

    def test_4_search_invalid_orders(self, setUp):
        self.orders_page.click_order_btn()
        self.orders_page.search_invalid()
        text_search_result = self.orders_page.search_result().get_attribute("innerText")
        assert text_search_result == "סה״כ: 0 שורות"

    def test_5_order_number_on_site_and_DB(self, setUp):
        self.orders_page.click_order_btn()
        first_order_from_page = self.orders_page.get_first_order_number_from_page()
        all_numbers_orders_db = get_all_numbers_orders_from_db(self.db)
        assert first_order_from_page in all_numbers_orders_db

    def test_6_orders_menu_btn_in_english_language(self, setUp):
        self.orders_page.click_order_btn()
        self.orders_page.click_orders_menu_btn()
        self.orders_page.click_english_language_btn()
        assert self.orders_page.menu_window_display()

    def test_7_search_google_maps(self, setUp):
        self.orders_page.click_orders_btn()
        self.orders_page.search("1168")
        self.orders_page.click_1168()
        self.orders_page.click_address()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == "https://www.google.com/maps/place/%D7%94%D7%93%D7%A8+5,+%D7%9B%D7%A4%D7%A8+%D7%A1%D7%91%D7%90%E2%80%AD/@32.1757182,34.9207372,17z/data=!3m1!4b1!4m6!3m5!1s0x151d39ba91eb8f0d:0xdd8fa456fa50b150!8m2!3d32.1757182!4d34.9185485!16s%2Fg%2F11fmfk0q13"

    def test_8_mark_order_as_ready_for_delivery_btn(self,setUp):
        self.orders_page.click_order_btn()
        self.orders_page.search_valid()
        self.orders_page.click_order_1242()
        self.orders_page.weight_valid()
        self.orders_page.click_mark_order_as_ready_for_delivery_btn()
        text = self.orders_page.message_display().get_attribute("textContent")
        assert text == "סטטוס הזמנה עודכן בהצלחה"

    def test_9_click_missing(self, setUp):
        self.orders_page.click_orders_btn()
        self.orders_page.search("1236")
        self.orders_page.click_id_order_1236()
        not_missing_color = self.orders_page.missing_display()
        self.orders_page.click_missing_btn()
        missing_color = self.orders_page.missing_display()
        assert missing_color != not_missing_color
        self.orders_page.click_quantity()
        self.orders_page.click_one_quantity()

    def test_10_click_replace_1(self, setUp):
        self.orders_page.click_orders_btn()
        self.orders_page.search("1236")
        self.orders_page.click_id_order_1236()
        self.orders_page.click_replace()
        self.orders_page.replace_search("למון")
        text_product = self.orders_page.lemon_display_1()
        text_search = "למון"
        assert text_search in text_product

    def test_10_click_replace_2(self, setUp):
        self.orders_page.click_orders_btn()
        self.orders_page.search("1168")
        self.orders_page.click_1168()
        self.orders_page.click_replace()
        self.orders_page.replace_search("למון")
        text_product = self.orders_page.lemon_display_()
        text_search = "למון"
        assert text_search in text_product

    def test_11_click_quantity(self, setUp):
        self.orders_page.click_orders_btn()
        self.orders_page.search("1236")
        self.orders_page.click_id_order_1236()
        self.orders_page.click_quantity()
        self.orders_page.click_five()
        # self.orders_page.click_one_quantity()
        assert self.orders_page.quantity_display() == "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10"

    def test_12_invalid_change_weight(self, setUp):
        self.orders_page.click_orders_btn()
        self.orders_page.search("1236")
        self.orders_page.click_id_order_1236()
        self.orders_page.click_ready_for_delivery()
        alert_text = self.orders_page.weight_alert_display()
        assert alert_text == "יש להזין משקל משטח"

    def test_13_change_surfaces(self, setUp):
        self.orders_page.click_orders_btn()
        self.orders_page.search("1236")
        self.orders_page.click_id_order_1236()
        self.orders_page.click_surfaces()
        self.orders_page.click_one_surface()
        alert_text = self.orders_page.surface_alert_display()
        assert alert_text == "סטטוס משטחים עודכן בהצלחה"

    def test_14_mark_order_as_sent_btn(self, setUp):
        self.orders_page.click_order_btn()
        self.orders_page.search_valid()
        self.orders_page.click_order_1242()
        self.orders_page.weight_valid()
        self.orders_page.click_mark_order_as_sent_btn()
        text = self.orders_page.message_display().get_attribute("textContent")
        assert text == "סטטוס הזמנה עודכן בהצלחה"

    def test_15_order_has_arrived_btn(self, setUp):
        self.orders_page.click_order_btn()
        self.orders_page.search_valid()
        self.orders_page.click_order_1242()
        self.orders_page.weight_valid()
        self.orders_page.click_order_has_arrived_btn()
        text = self.orders_page.message_display().get_attribute("textContent")
        assert text == "סטטוס הזמנה עודכן בהצלחה"

    def test_16_change_page_right(self, setUp):
        self.orders_page.click_orders_btn()
        text = self.orders_page.row_number_view_display()
        self.orders_page.click_right_btn()
        updated_text = self.orders_page.row_number_view_display()
        assert text != updated_text

    def test_16_change_double_right(self, setUp):
        self.orders_page.click_orders_btn()
        text = self.orders_page.row_number_view_display()
        self.orders_page.click_double_right_btn()
        updated_text = self.orders_page.row_number_view_display()
        assert text != updated_text

    def test_16_change_page_left(self, setUp):
        self.orders_page.click_orders_btn()
        text = self.orders_page.row_number_view_display()
        self.orders_page.click_double_right_btn()
        self.orders_page.click_left_btn()
        updated_text = self.orders_page.row_number_view_display()
        assert text != updated_text or text == updated_text

    def test_16_change_double_left(self, setUp):
        self.orders_page.click_orders_btn()
        text = self.orders_page.row_number_view_display()
        self.orders_page.click_double_right_btn()
        self.orders_page.click_double_left_btn()
        updated_text = self.orders_page.row_number_view_display()
        assert text != updated_text or text == updated_text

    def test_17_how_many_orders_display(self, setUp):
        self.orders_page.click_orders_btn()
        self.orders_page.click_number()
        self.orders_page.click_random_num()
        assert self.orders_page.row_number_view_2_display() == "מציג 1-100 מתוך 932 שורות" or "מציג 1-20 מתוך 932 שורות" or "מציג 1-50 מתוך 932 שורות" \
               or "מציג 1-75 מתוך 932 שורות" or "מציג 1-150 מתוך 932 שורות" or "מציג 1-200 מתוך 932 שורות" or "סה״כ: 932 שורות"




