from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import allure

'''
Этот файл содержит класс KinoPage, который предоставляет методы для автоматизации взаимодействия
с веб-сайтом Кинопоиска с использованием Selenium. Класс позволяет выполнять поиск фильмов, жанров, стран и годов выпуска.
'''


class KinoPage:
    def __init__(self, browser):
        with allure.step("Инициализируем браузер"):
            '''
            Описание: Конструктор класса. Инициализирует браузер и базовый URL сайта Кинопоиска.
            Параметры:
            browser: Объект браузера, созданный с помощью Selenium.
            Атрибуты:
            __browser: Объект браузера.
            __url (str): Базовый URL сайта Кинопоиска.
            '''
        self.__browser = browser
        self.__url = "https://www.kinopoisk.ru/"

    def go_start_page(self):
        with allure.step("Переходим на страницу сайта"):
            self.__browser.get(self.__url)

    def search_movie(self, name: str):
        with allure.step("Поиск фильма по названию"):

            '''
            Описание: Выполняет поиск фильма по названию на сайте Кинопоиска.
            Параметры:
            name (str): Название фильма.
            Возвращает:
            int: Количество найденных результатов.
            '''
            with allure.step("Находим поисковую строку"):
                input_field = self.__browser.find_element(By.XPATH, '//input[@name="kp_query"]')
            with allure.step("Вводим название в поисковую строку"):
                input_field.send_keys(name, Keys.RETURN)
            with allure.step("Берем текст последнего элемента поиска"):
                search_str = self.__browser.find_element(By.CSS_SELECTOR, '.search_results_topText').text
                return int(search_str.split('результаты: ')[-1])

    def search_genres(self, name_genre: str):

        '''
        Описание: Выполняет поиск фильмов по жанру.
        Параметры:
        name_genre (str): Название жанра.
        Возвращает:
        bool: True, если фильмы найдены, иначе None.
        '''
        # Переходим на страницу с категориями фильмов
        with allure.step("Переходим на страницу жанров"):
            self.__browser.get(self.__url + "/lists/categories/movies/1/")
            # Ищем ссылку на страницу с жанрами
        with allure.step("Поиск элемента на странице 'Жанры'"):
            elem = self.__browser.find_element(By.XPATH, "//a[text()='Жанры']")
            href = elem.get_attribute('href')

        # Переходим на страницу с жанрами
        with allure.step("Переход на страницу жанров"):
            self.__browser.get(href)
        # Ищем элемент с указанным жанром
        try:
            with allure.step("Поиск нужного жанра в списке"):
                # Используем переменную name_genre для поиска нужного жанра
                element = self.__browser.find_element(By.XPATH, f"//span[text()='{name_genre}']/ancestor::a")
                href = element.get_attribute('href')  # Возвращаем текст найденного элемента
            with allure.step("Переход на страницу выбранного жанра"):
                self.__browser.get(href)
            with allure.step("Проверяем есть ли на странице элементы, удовлетворяющие условиям"):
                movie_element = self.__browser.find_element(By.XPATH, f"//a[contains(@href, '/film/')]")
                if not movie_element:
                    movie_element = self.__browser.find_element(By.XPATH, f"//a[contains(@href, '/series/')]")
                return movie_element is not None
        except Exception as e:
            print(f"Жанр '{name_genre}' не найден: {e}")
            return None  # Возвращаем None, если жанр не найден

    def search_countries(self, name_country: str):

        with allure.step("Переход на страницу 'Страны'"):
            '''
            Описание: Выполняет поиск фильмов по стране производства.
            Параметры:
            name_country (str): Название страны.
            Возвращает:
            bool: True, если фильмы найдены, иначе None.
            '''
            self.__browser.get(self.__url + "/lists/categories/movies/9/")
        with allure.step("Находим на странице элемент для перехода к странам"):
            elem_country = self.__browser.find_element(By.XPATH, "//a[text()='Страны']")
            href_country = elem_country.get_attribute('href')
        with allure.step("Переходим во вкладку 'Страны'"):
            self.__browser.get(href_country)
        try:
            # Используем переменную name_country для поиска нужной страны
            with allure.step("Поиск элемента на странице - конкретной страны"):
                countries = self.__browser.find_element(By.XPATH, f"//span[text()='{name_country}']/ancestor::a")
                href = countries.get_attribute('href')  # Возвращаем текст найденного элемента
            with allure.step("Переходим на страницу с выбранной страной"):
                self.__browser.get(href)
            with allure.step("Ищем элементы, удовлетворяющие условиям"):
                country_element = self.__browser.find_element(By.XPATH, f"//a[contains(@href, '/film/')]")
                if not country_element:
                    country_element = self.__browser.find_element(By.XPATH, f"//a[contains(@href, '/series/')]")
                return country_element is not None
        except Exception as e:
            print(f"Страны '{name_country}' не найден: {e}")
            return None  # Возвращаем None, если жанр не найден

    def search_years(self, years: int):

        with allure.step("Переход на страницу категории 'Годы'"):
            '''
            Описание: Выполняет поиск фильмов по году выпуска.
            Параметры:
            years (int): Год выпуска.
            Возвращает:
            bool: True, если фильмы найдены, иначе None.
            '''
            self.__browser.get(self.__url + "/lists/categories/movies/7/")
        with allure.step("Находим на странице элемент для перехода к категории 'Годы'"):
            elem_year = self.__browser.find_element(By.XPATH, "//a[text()='Годы']")
            href_year = elem_year.get_attribute('href')
        with allure.step("Переходим на страницу фильтра по годам"):
            self.__browser.get(href_year)
        try:
            # Используем переменную year для поиска нужного года
            with allure.step("Поиск конкретного года для поиска"):
                year = self.__browser.find_element(By.XPATH, f"//a[contains(@href, '/lists/movies/year--{years}/')]")
                href = year.get_attribute('href')  # Возвращаем текст найденного элемента
            with allure.step("Переход на страницу нужного года"):
                self.__browser.get(href)
            with allure.step("Поиск элементов, удовлетворяющих условиям"):
                year_element = self.__browser.find_element(By.XPATH, f"//a[contains(@href, '/film/')]")
                if not year_element:
                    year_element = self.__browser.find_element(By.XPATH, f"//a[contains(@href, '/series/')]")
                return year_element is not None
        except Exception as e:
            print(f"Год '{years}' не найден: {e}")
            return None  # Возвращаем None, если год не найден

    def search_navigator(self, filter: dict):
        self.__browser.get(self.__url)

        with allure.step("Переход на страницу навигатора поиска"):
            '''
            Описание: Выполняет поиск фильмов с использованием фильтров (жанр, страна, год) на странице навигатора Кинопоиска.
            Параметры:
            filter (dict): Словарь с фильтрами (например, {'genre': 'боевик', 'country': 'США', 'year': '2020'}).
            Возвращает:
            WebElement: Элемент с результатами поиска, или None, если фильтр не найден.
            '''
            self.__browser.get(self.__url + "/top/navigator/")
        with allure.step("Находим на странице элемент 'Жанры', разворачиваем список жанров"):
            # Задан ли жанр
            if ((genre := filter.get('genre', '')) != ''):
                genre_list = self.__browser.find_element(By.XPATH, '//div[@id="genreListTitle"]')
                genre_list.click()
        with allure.step("Выбор в выпадающем списке жанра"):
            s_genre = f"//ul[@id='genreList']//li[contains(@class, 'selectItem')]//label[contains(text(), '{genre}')]/input"
            self.__browser.find_element(By.XPATH, s_genre).click()
            genre_list.click()
            sleep(2)
        with allure.step("Находим на странице элемент 'Страны', разворачиваем список стран"):
            # Задана ли страна
            if ((country := filter.get('country', '')) != ''):
                country_list = self.__browser.find_element(By.XPATH, '//div[@id="countryListTitle"]')
                country_list.click()
        with allure.step("Выбор в выпадающем списке страны"):
            s_country = f"//ul[@id='countryList']//li[contains(@class, 'selectItem')]//label[contains(text(), '{country}')]/input"
            self.__browser.find_element(By.XPATH, s_country).click()
            country_list.click()
            sleep(2)
        with allure.step("Находим на странице элемент 'Годы', разворачиваем список"):
            # Задан ли год
            if ((year := filter.get('year', '')) != ''):
                year_list = self.__browser.find_element(By.XPATH, '//select[@class="wide year_select"]')
                year_list.click()
        with allure.step("Выбор из списка конкретного года"):
            try:
                s_year = f"//select[@class='wide year_select']/option[@value='{year}']"
                self.__browser.find_element(By.XPATH, s_year).click()
                year_list.click()
                sleep(2)
            except Exception as e:
                print(f"Год '{year}' не найден: {e}")
                return None  # Возвращаем None, если год не найден
        with allure.step("Находим и нажимаем кнопку 'Поиск'"):
            # Ищем кнопку Поиск
            search_button = self.__browser.find_element(By.XPATH, '//input[@type="button" and @value="поиск"]')
            search_button.click()

            sleep(5)

            result_elements = self.__browser.find_element(By.XPATH, '//div[@id="results"]/*')
            return result_elements
