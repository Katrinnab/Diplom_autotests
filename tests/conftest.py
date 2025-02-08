import pytest
from selenium import webdriver
from pages.authpage import AuthPage
from pages.uipage import KinoPage

'''
Этот файл содержит фикстуры для тестов. Фикстуры используются для настройки и
управления состоянием тестов, такими как инициализация браузера и создание
объектов для работы с API и веб-интерфейсом.
'''

token = '3P4E8WS-TEE43NZ-G6BMETR-52NFY0A'
cookie_string = 'yashr=3416631591727972306; mda_exp_enabled=1; yandexuid=7716674971708609462; gdpr=0; _ym_uid=1727972308837301946; yuidss=7716674971708609462; my_perpages=%5B%5D; no-re-reg-required=1; mobile=no; i=71gOQDsPyYTxD1FhWn7oQDB6z45PCO4jxArJXGrjvnboI3LJwhQgtlwdbu5HhZa+Lul/yLxIRX2avcWJ3zRKO/ztJEk=; desktop_session_key=755a77a886d89fe709c523e41db97c7441a58e1a2ca075cbd1898383d6bedb81bd62fcf1e5bec2cb7579a291e45f4ae699a828a92c4e04911f87c81c93466f67c7581db2c2e9cbe145b4f74efdb29754c892317f833072cc90c8b482617cf770baf4364369df56feff1c97c2a3810543bb2aedb51edbac8ab71094983ca2c45f21695b7dab0e1dcf4435c8c8605d88adbb3fba6dfff2d2ef9d337a9c011cc2c54493a80fd81e4956e3000b8938646e7e; desktop_session_key.sig=RM4Vg8GKj3v-7X56aiq9p6Io0O0; _csrf=elAK3wUXQmTq0RhoqH14QF90; PHPSESSID=4e72be8c38aff3c58c8fa18b7808cb30; user-geo-region-id=2; user-geo-country-id=2; _ym_isad=2; _csrf_csrf_token=sQshSKz84KdZOOosrEPWE8qC7Sxev23LLzGnhNMjP_s; yp=1739038874.yu.7716674971708609462; ymex=1741544474.oyu.7716674971708609462; disable_server_sso_redirect=1; _yasc=ZvtOHAwrOUdyrm6qoaoaohO+MEL+Fx0nb5ow5t5IQz1Rk0HVUqj5AsLq6+Qi0/Nf7w==; sso_status=sso.passport.yandex.ru:synchronized; ya_sess_id=3:1739011261.5.0.1739011259982:50MgLg:ed40.1.2:1|303768691.-1.2.3:1739011259|30:10232354.202301.VxKyUhqSy-gXBUoW3a6hrFoF8EY; sessar=1.1198.CiDheWSjuxWZ9rPXcrBU081mFicV3fxw8-7dOEwZxwtnoQ.ruPC4z-PqyFY3W7hukJdE-aMiHuxaumaFUGrg9-PFls; yandex_login=KatrinNab; ys=c_chck.3100583846#udn.cDpLYXRyaW5OYWI%3D; L=YWx+AUtcdV1QUXdPRwBiUnl3ZAdHZAF4eQJGF1E7IikW.1739011259.16048.323767.cea326f7a029af47cc3b3672fd96cdc1; mda2_beacon=1739011261488; _ym_visorc=b; uid=20276322; _ym_d=1739011713; sgst=searchRequest-%D0%B0%D0%B2%D0%B0%D1%82%D0%B0%D1%80; cycada=zrWZ9wRHpIukTz6Mq5y9NhGDEi26wU4MUjHeDo4cbWQ='
base_url = "https://www.kinopoisk.ru/"


def parse_cookie(cookie_string):
    cookies = []
    for cookie in cookie_string.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies.append({'name': name, 'value': value, 'path': '/'})
    return cookies


cookies = parse_cookie(cookie_string)


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
    browser.get(base_url)

    for cookie in cookies:
        browser.add_cookie(cookie)
    ui_page = KinoPage(browser)
    yield ui_page
