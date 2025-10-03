from base.base_method import BaseMethod
from tests.data.user_data import UsersData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from page.make_order_page import MakeOrders


class ClientField(BaseMethod):
    def __init__(self, driver, user):
        super().__init__(driver)
        self.user = user  # здесь просто сохраняем ссылку на UsersData

    #locators
    NAME = (By.XPATH, "//input[@id='billing_first_name']")
    LAST_NAME = (By.XPATH, "//input[@id='billing_last_name']")
    COUNTRY = (By.XPATH, "//span[@id='select2-billing_country-container']")  # там выпадашка
    INPUT_COUNTRY = (By.XPATH, "//input[@class='select2-search__field']")
    ADDRESS = (By.XPATH, "//input[@id='billing_address_1']")
    CITY = (By.XPATH, "//input[@id='billing_city']")
    STATE = (By.XPATH, "//input[@id='billing_state']")
    POSTAL_CODE = (By.XPATH, "//input[@id='billing_postcode']")
    PHONE = (By.XPATH, "//input[@id='billing_phone']")
    EMAIL = (By.XPATH, "//input[@id='billing_email']")
    TYPE_PAYMENT = (By.XPATH, "//label[@for='payment_method_cod']")
    APPROVAl_ORDER = (By.XPATH, "//input[@id='place_order']")
    TOTAL_PRICE = (By.XPATH, "(//span[@class='woocommerce-Price-amount amount'])[1]")  # тут 2,990
    TYPE_DELIVERY2 = (By.XPATH, "//label[@for='shipping_method_0_local_pickup-4']")

    #getters
    def get_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.NAME)
        )

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.LAST_NAME)
        )

    def get_country(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.COUNTRY)
        )

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.ADDRESS)
        )

    def get_input_country(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.INPUT_COUNTRY)
        )

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.CITY)
        )

    def get_state(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.STATE)
        )

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.POSTAL_CODE)
        )

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.PHONE)
        )

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.EMAIL)
        )

    def get_type_payment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.TYPE_PAYMENT)
        )

    def get_approval_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.APPROVAl_ORDER)
        )

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.TOTAL_PRICE)
        )

    def get_type_delivery2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.TYPE_DELIVERY2)
        )

    # actions
    def input_name(self):
        self.send_keys(self.get_name(), self.user.name)

    def input_last_name(self):
        self.send_keys(self.get_last_name(), self.user.last_name)

    def click_country(self):
        self.click_webelement(self.get_country())

    def input_country(self):
        self.send_keys(self.get_input_country(), self.user.country)

    def input_address(self):
        self.send_keys(self.get_address(), self.user.address)

    def input_city(self):
        self.send_keys(self.get_city(), self.user.city)

    def input_state(self):
        self.send_keys(self.get_state(), self.user.state)

    def input_postal_code(self):
        self.send_keys(self.get_postal_code(), self.user.postal_code)

    def input_phone(self):
        self.send_keys(self.get_phone(), self.user.phone)

    def input_email(self):
        self.send_keys(self.get_email(), self.user.email)

    def text_type_delivery(self):
        type_delivery2 = self.get_type_delivery2().text

    def click_button_approval_order(self):
        self.click_webelement(self.get_approval_order())

    # method
    def make_order(self):
        self.input_name()
        self.input_last_name()
        self.click_country()
        self.input_country()  # ввели название страны
        self.click_key_enter(self.get_input_country())  # клик клавишей
        self.input_address()
        self.input_city()
        self.input_state()
        self.input_postal_code()
        self.input_phone()
        self.input_email()
        print('Ввели данные получателя!')
        self.click_button_approval_order()

    def check_text_type_delivery_2(self):
        text_type_delivery_2 = self.get_type_delivery2().text
        return text_type_delivery_2
