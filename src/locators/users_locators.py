from selenium.webdriver.common.by import By


class UserLocators:
    user_main_menu_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/nav/div[2]/a[24]')
    user_search_bar = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/span/span/div/input')
    user_search_1st_output = (
    By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]')
    #three_dots_left_side = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/main/div[2]/div/div[1]/div/span/i')
    three_dots_left_side= (By.XPATH,"/html/body/div/div[1]/div[2]/main/div[2]/div/div[1]/div/span")
    add_btn = (By.XPATH,"/html/body/div/div[1]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[1]/span[1]/i")
    input_first_name = (By.XPATH,"/html/body/div/div[1]/div[4]/div/div/form/div[1]/div[1]/span/div/input")
    input_last_name = (By.XPATH,"/html/body/div/div[1]/div[4]/div/div/form/div[1]/div[2]/span/div/input")
    input_email = (By.XPATH,"/html/body/div/div[1]/div[4]/div/div/form/div[1]/div[3]/span/div/input")
    error_message_email = (By.XPATH,"/html/body/div/div[1]/div[4]/div/div/form/div[1]/div[3]/div")
    input_phone = (By.XPATH,"/html/body/div/div[1]/div[4]/div/div/form/div[1]/div[4]/span/div/input")
    error_message_phone = (By.XPATH,"/html/body/div/div[1]/div[4]/div/div/form/div[1]/div[4]/div")
    search_result = "/html/body/div/div[1]/div[2]/main/div[2]/div/div[2]/div[2]/div[2]"
