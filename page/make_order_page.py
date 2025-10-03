from base.base_method import BaseMethod
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException

class MakeOrders(BaseMethod):
    #locators
    DELIVERY_YOURSELF = (By.XPATH, "//label[@for='shipping_method_0_local_pickup-4']")
    PRICE_CHECK = (By.XPATH, "(//span[@class='woocommerce-Price-amount amount'])[3]")
    BUTTON_ORDER = (By.XPATH, "//a[contains(@class,'checkout-button button alt')]")
    TYPE_DELIVERY = (By.XPATH, "//label[@for='shipping_method_0_local_pickup-4']")

    #getters

    def get_delivery_yourself(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.DELIVERY_YOURSELF)
        )

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.PRICE_CHECK)
        )

    def get_button_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.BUTTON_ORDER)
        )

    def get_type_delivery(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.TYPE_DELIVERY)
        )

    # actions
    def select_delivery_product(self):
        self.click_webelement(self.get_delivery_yourself())  # после этого перерисовывается DOM
        try:
            self.click_webelement(self.get_button_order())
            assert self.check_url() == 'https://weareurals.ru/checkout/', 'Ошибка: нет редиректа на страницу заполнения данных получателя'
            print('Успешно: редирект на страницу заполнения данных получателя!')

        except StaleElementReferenceException:
            self.get_button_order()  # принудительно еще раз ищем кнопку Оформить заказ, т.к. выбор чекбокса доставки перерисовал ДОМ
            self.click_webelement(self.get_button_order())
            assert self.check_url() == 'https://weareurals.ru/checkout/', 'Ошибка: нет редиректа на страницу заполнения данных получателя'
            print('Успешно: редирект на страницу заполнения данных получателя!')

        except ElementClickInterceptedException:
            self.get_button_order()  # принудительно еще раз ищем кнопку Оформить заказ, т.к. выбор чекбокса доставки перерисовал ДОМ
            self.click_webelement(self.get_button_order())
            assert self.check_url() == 'https://weareurals.ru/checkout/', 'Ошибка: нет редиректа на страницу заполнения данных получателя'
            print('Успешно: редирект на страницу заполнения данных получателя!')


    def check_type_delivery(self):
        type_delivery = self.get_type_delivery().text
        return type_delivery

