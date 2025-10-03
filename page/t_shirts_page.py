from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_method import BaseMethod


class TShirts(BaseMethod):
    # locators
    BUTTON_SHOP = (By.XPATH, "(//a[@title='Магазин'])[3]")  # (//a[@title='Магазин'])[3]
    TSHiRT_NUMBER_5 = (By.CSS_SELECTOR, " .first.post-21727.product")  # черная
    PRICE_TSHiRT_NUMBER_5 = (By.XPATH, "(//span[@class='price'])[9]")

    # getters
    def enter_shop(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.BUTTON_SHOP)
        )

    def enter_tshirt(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.TSHiRT_NUMBER_5)
        )

    def enter_tshirt_price(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.PRICE_TSHiRT_NUMBER_5)
        )

    # actions
    def select_tshirt(self):
        self.open_site("https://weareurals.ru/")
        self.click_webelement(self.enter_shop())
        self.assert_text(self.enter_tshirt_price(), '2,590')
        self.click_webelement(self.enter_tshirt())
