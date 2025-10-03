import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def init_driver():
    path_chrome_driver = Service(r"C:\Sonya_Work\chrome_driver_direct\chromedriver.exe")
    options = Options()
    options.add_argument("--window-size=1920,1080")
    # options.add_argument("--headless")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=path_chrome_driver, options=options)
    yield driver
    driver.quit()


