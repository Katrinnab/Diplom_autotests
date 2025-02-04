from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class KinoPage:
    def __init__(self, browser):
        self.__browser = browser
        self.__url = "https://www.kinopoisk.ru/"

    def go_start_page(self):
        self.__browser.get(self.__url)

    def search_movie(self, name):
        self.__browser.get(self.__url)
        WebDriverWait(self.__browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@name="kp_query"]')))        
        input_field = self.__browser.find_element(By.XPATH, '//input[@name="kp_query"]')
        input_field.send_keys(name)
        sleep(6)
        # search_field = self.__browser.find_element(By.CSS_SELECTOR, '.bEOAU8l0RAVCYGLwzIcd search-form-submit-button__icon')
        # search_field.click()
        