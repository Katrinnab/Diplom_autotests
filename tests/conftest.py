import pytest
from selenium import webdriver
from pages.authpage import AuthPage

token = '3P4E8WS-TEE43NZ-G6BMETR-52NFY0A'


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def main_page(browser):
    auth_page = AuthPage(browser, token)
    yield auth_page
