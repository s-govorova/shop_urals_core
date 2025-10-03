from base.base_method import BaseMethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductDescription(BaseMethod):
    #locators
    SIZE_M = (By.XPATH, "//li[@data-wvstooltip='M']")
    BUTTON_IN_CART = (By.XPATH, "//button[contains(@class, 'single_add_to_cart_button')]")
    MESSAGE_BUY_PRODUCT = (By.CSS_SELECTOR, ".woocommerce-message")
    BUTTON_CART = (By.XPATH, "//a[@class='minicart-link']")

    #getter
    def get_size_m(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.SIZE_M)
        )

    def get_button_in_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.BUTTON_IN_CART)
        )

    def get_message_buy(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.MESSAGE_BUY_PRODUCT)
        )

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.BUTTON_CART)
        )

    # actions
    def select_size_tshirt(self):
        self.click_webelement(self.get_size_m())
        self.click_webelement(self.get_button_in_cart())

    # method
    def check_tshirt_in_cart(self):
        self.select_size_tshirt()
        # для чего эта конструкция: время от времени элемент уведомления либо находится сразу, либо длительное время таймауты, уместно ли здесь оставлять повторные действия через обработку исключения?
        try:
            if self.get_message_buy():
                print('Появилось уведомление, что товар в корзине!')
        except TimeoutException:
            if self.get_message_buy():
                print('Появилось уведомление, что товар в корзине!')

        self.click_webelement(self.get_button_cart())
        assert self.check_url() == 'https://weareurals.ru/cart/', 'Ошибка: нет редиректа со страницы описания товара >> на страницу оформления заказа'
        print('Успешно: произошел редирект на страницу оформления заказа')



