from base.base_method import BaseMethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class ThanksForOrder(BaseMethod):
    #locators
    DATA_ORDER = (By.XPATH, "//li[contains(@class,'date')]/strong")

    # getter
    def get_data_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.DATA_ORDER)
        )

    # actions

    # methods

    def check_info_success_order(self):
        data_today_full = datetime.now()
        data_today = data_today_full.strftime("%d.%m.%Y")
        assert self.get_data_order().text == data_today, f'Ошибка: дата оформления заказа не совпадает с текущим днем: {self.get_data_order().text}'
        print(f'Тесты ок: дата оформления заказа совпадает с текущим днем: {self.get_data_order().text}')




