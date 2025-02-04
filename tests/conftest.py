import pytest
from selenium import webdriver
from pages.authpage import AuthPage
from pages.uipage import KinoPage

token = '3P4E8WS-TEE43NZ-G6BMETR-52NFY0A'


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def main_page():
    auth_page = AuthPage(token)
    yield auth_page


@pytest.fixture()
def kino_page(browser):
    ui_page = KinoPage(browser)
    yield ui_page
