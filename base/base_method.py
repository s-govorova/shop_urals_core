from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
class BaseMethod:

    def __init__(self, driver):
        self.driver = driver

    def open_site(self, site_link):
        '''Метод для перехода на сайт'''
        self.driver.get(site_link)

    def check_url(self):
        '''Метод возвращает текущее url'''
        return self.driver.current_url

    def assert_text(self, locator, word):
        '''Метод принимает локатор, у которого достает текст и проверочное слово. Данные сравниваются'''
        result_txt = locator.text
        assert result_txt == word, f'Искомый текст: {result_txt} не совпадает'
        print(f'Искомый текст: {result_txt} совпадает!')

    def click_webelement(self, webelement):
        webelement.click()

    def send_keys(self, webelement, data):
        webelement.send_keys(data)

    def click_key_enter(self, webelement):
        '''Метод клика клавиши ENTER'''
        key = Keys()
        webelement.send_keys(key.ENTER)


    def screenshot_finish_test(self):
        '''Создание скриншота по окончании тестов'''
        part_name_screen = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = 'screen' + part_name_screen + '.png'
        self.driver.save_screenshot(f"C:\\Sonya_Work\Shop_Urals\\screenshot\\{name_screenshot}")
        print('Скриншот по окончании тестов сохранен!')



