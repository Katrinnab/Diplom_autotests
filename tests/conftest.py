import pytest
from selenium import webdriver
from pages.authpage import AuthPage
from pages.uipage import KinoPage

'''
Этот файл содержит фикстуры для тестов. Фикстуры используются для настройки и
управления состоянием тестов, такими как инициализация браузера и создание
объектов для работы с API и веб-интерфейсом.
'''

token = 'здесь твой токен'
base_url = "https://www.kinopoisk.ru/"


@pytest.fixture()
def browser():
    '''
    Описание: Инициализирует и настраивает браузер для тестов веб-интерфейса.
    Возвращает:
    Объект браузера (например, webdriver.Chrome).
    Действия:
    Настраивает опции браузера.
    Устанавливает неявное ожидание (5 секунд).
    Максимизирует окно браузера.
    После завершения теста закрывает браузер.
        '''
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def main_page():
    '''
    Описание: Создает объект AuthPage для работы с API Кинопоиска.
    Возвращает:
    Объект AuthPage, инициализированный с токеном.
    Примечание:
    Токен для доступа к API Кинопоиска задан в переменной token.
    '''
    auth_page = AuthPage(token)
    yield auth_page


@pytest.fixture()
def kino_page(browser):
    '''
    Описание: Создает объект KinoPage для работы с веб-интерфейсом Кинопоиска.
    Параметры:
    browser: Объект браузера, созданный фикстурой browser().
    Возвращает:
    Объект KinoPage, инициализированный с браузером.
    '''
    ui_page = KinoPage(browser)
    yield ui_page
