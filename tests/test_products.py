from time import sleep
from src.utils.db import is_product_in_db, get_price_from_db_by_barcode, get_name_from_db_by_barcode, \
    get_description_from_db_by_barcode, get_barcode_from_db_by_barcode
from src.utils.setup import WebDriverSetup

class TestTrado(WebDriverSetup):

    def test_1_search_valid_product_display_first(self, setUp):
        self.products_page.click_products_btn()
        product_name_in_db = self.products_page.get_product_name_to_search(self.db)
        self.products_page.search_bar_keyword(product_name_in_db)
        product_name_on_page = self.products_page.get_product_name()
        assert product_name_in_db == product_name_on_page


    def test_2_search_invalid_product(self, setUp):
        self.products_page.click_products_btn()
        self.products_page.search_bar_keyword('ghgjnfnfmf')
        is_no_result_text_display = self.products_page.get_no_results_text()
        assert is_no_result_text_display == 'סה״כ: 0 שורות'

    def test_3_product_name_on_site_and_db(self, setUp):
        self.products_page.click_products_btn()
        name_from_page = self.products_page.get_product_name_from_page()
        barcode_from_page = self.products_page.get_barcode_from_page()
        name_from_db = get_name_from_db_by_barcode(self.db, barcode_from_page)
        assert name_from_page == name_from_db

    def test_4_product_price_on_site_and_db(self, setUp):
        self.products_page.click_products_btn()
        price_from_page = self.products_page.get_product_price_from_page()
        barcode_from_page = self.products_page.get_barcode_from_page()
        price_from_db = get_price_from_db_by_barcode(self.db, barcode_from_page)
        assert price_from_page == price_from_db

    def test_5_valid_transition_between_pages(self, setUp):
        self.products_page.click_products_btn()
        barcode_from_first_page = self.products_page.get_barcode_from_page()
        self.products_page.click_next_product_page()
        barcode_from_second_page = self.products_page.get_barcode_from_page()
        assert barcode_from_first_page != barcode_from_second_page

    def test_6_valid_amount_of_products_on_page(self, setUp):
        self.products_page.click_products_btn()
        self.products_page.click_on_product_amount_option()
        self.products_page.click_on_20_products_on_page_option()
        barcodes = self.products_page.get_all_barcodes_from_page()
        assert len(barcodes) == 20

    def test_7_add_valid_product(self, setUp):
        self.products_page.click_products_btn()
        self.products_page.click_products_menu()
        self.products_page.click_add_product_btn()
        barcode = '8397'
        self.products_page.input_product_barcode(barcode)
        self.products_page.upload_photo_to_product()
        self.products_page.input_product_name('mufleta')
        self.products_page.input_product_price('100')
        self.products_page.input_product_sale_price('100')
        self.products_page.click_next_btn()
        self.products_page.click_product_category()
        self.products_page.click_category_first_option()
        self.products_page.click_store_field()
        self.products_page.click_store_first_option()
        self.products_page.click_next_btn()
        self.products_page.click_and_input_unitsincarton('50')
        self.products_page.click_next_btn()
        self.products_page.click_next_btn()
        is_product_created = is_product_in_db(self.db, barcode)
        assert is_product_created == True


    # def test_8_edit_product_description(self, setUp):
    #     self.products_page.click_products_btn()
    #     self.products_page.click_edit_product_description()
    #     self.products_page.delete_text_on_description_popup()
    #     text_to_insert = 'new text'
    #     self.products_page.input_text_to_description_field(text_to_insert)
    #     self.products_page.click_save_description_btn()
    #     barcode_from_page = self.products_page.get_barcode_from_page()
    #     description_on_db = get_description_from_db_by_barcode(self.db, barcode_from_page)
    #     assert text_to_insert == description_on_db
    #     # Todo: waiting for israel's answer


    def test_9_add_product_with_exist_barcode_invalid(self, setUp):
        self.products_page.click_products_btn()
        self.products_page.click_products_menu()
        self.products_page.click_add_product_btn()
        barcode_from_db = get_barcode_from_db_by_barcode(self.db)
        self.products_page.input_product_barcode(barcode_from_db)
        barcode_error_msg = self.products_page.is_barcode_error_msg_display()
        assert barcode_error_msg.is_displayed() == True and barcode_error_msg.text == 'הברקוד שהוזן קיים במערכת'


    def test_10_error_msg_display_without_barcode_on_add_product(self, setUp):
        self.products_page.click_products_btn()
        self.products_page.click_products_menu()
        self.products_page.click_add_product_btn()
        self.products_page.input_product_name('mufleta')
        self.products_page.input_product_price('100')
        self.products_page.input_product_sale_price('100')
        self.products_page.click_next_btn()
        barcode_error_msg = self.products_page.is_barcode_error_msg_display()
        assert barcode_error_msg.is_displayed() == True and barcode_error_msg.text == 'נא למלא שדה זה'





