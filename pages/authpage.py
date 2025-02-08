import requests
import allure

'''
Этот файл содержит класс AuthPage, который предоставляет методы для взаимодействия с API Кинопоиска.
Класс использует библиотеку requests для выполнения HTTP-запросов к API.
'''


class AuthPage:
    def __init__(self, token: str):
        with allure.step("Инициализируем браузер, передаем токен"):
            '''
            Описание: Конструктор класса. Инициализирует базовый URL API и токен для авторизации.
            Параметры:
            token (str): Токен для доступа к API Кинопоиска.
            Атрибуты:
            __url (str): Базовый URL API Кинопоиска.
            __token (str): Токен для авторизации.
            '''
            self.__url = 'https://api.kinopoisk.dev/v1.4'
            self.__token = token

    def search_for_id(self, id):
        with allure.step("Выполняем поиск по id фильма get запросом"):
            '''
            Описание: Выполняет поиск фильма по его ID.
            Параметры:
            id (int или str): ID фильма.
            Возвращает:
            dict: JSON-ответ от API с информацией о фильме.
            '''
            headers = {
                        'X-API-KEY': self.__token
                        }
            response = requests.get(self.__url + f'/movie/{str(id)}',
                                    headers=headers)
            return response.json()

    def search_by_name(self, name: str):
        with allure.step("Выполняем поиск по названию фильма get запросом"):
            '''
            Описание: Выполняет поиск фильмов по названию.
            Параметры:
            name (str): Название фильма.
            Возвращает:
            dict: JSON-ответ от API с результатами поиска.
            '''
            headers = {
                        'X-API-KEY': self.__token
                        }
            response = requests.get(self.__url +
                                    f'/movie/search?page=1&limit=10&query={name}',
                                    headers=headers)
            return response.json()

    def search_by_type(self, type: str):
        with allure.step("Выполняем поиск по типу фильма get запросом"):
            '''
            Описание: Выполняет поиск фильмов по типу (например, фильм, сериал).
            Параметры:
            type (str): Тип контента (например, "movie", "tv-series").
            Возвращает:
            dict: JSON-ответ от API с результатами поиска.
            '''
            headers = {
                        'X-API-KEY': self.__token
                        }
            response = requests.get(self.__url +
                                    f'/movie?page=1&limit=10&type={type}',
                                    headers=headers)
            return response.json()

    def search_by_feature_date(self, date: str):
        with allure.step("Выполняем поиск фильма по невалидной дате get запросом"):
            '''
            Описание: Выполняет поиск фильмов по году выпуска.
            Параметры:
            date (str): Год выпуска фильма.
            Возвращает:
            dict: JSON-ответ от API с результатами поиска.
            '''
            headers = {
                        'X-API-KEY': self.__token
                        }
            response = requests.get(self.__url + f'/movie?year={date}',
                                    headers=headers)
            return response.json()

    def search_by_year_and_genres(self, year: int, genre: str):
        with allure.step("Выполняем поиск фильма по году и жанру get запросом"):
            '''
            Описание: Выполняет поиск фильмов по году выпуска и жанру.
            Параметры:
            year (int): Год выпуска фильма.
            genre (str): Название жанра.
            Возвращает:
            dict: JSON-ответ от API с результатами поиска.
            '''
            headers = {
                        'X-API-KEY': self.__token
                        }
            response = requests.get(self.__url + f'/movie?year={year}&genres.name={genre}',
                                    headers=headers)
            return response.json()

    def search_by_invalid_rating(self, rating: int):
        with allure.step("Выполняем поиск фильма по невалидному рейтингу get запросом"):
            '''
            Описание: Выполняет поиск фильмов по рейтингу IMDb.
            Параметры:
            rating (int): Рейтинг IMDb.
            Возвращает:
            dict: JSON-ответ от API с результатами поиска.
            '''
            headers = {
                        'X-API-KEY': self.__token
                        }
            response = requests.get(self.__url + f'/movie?rating.imdb={rating}',
                                    headers=headers)
            return response.json()

    def search_by_year_age_country(self, year: int, age: int, country: str):
        with allure.step("Выполняем поиск фильма по году выпуска, возрасту и стране get запросом"):
            '''
            Описание: Выполняет поиск фильмов по году выпуска, возрастному рейтингу и стране.
            Параметры:
            year (int): Год выпуска фильма.
            age (int): Возрастной рейтинг.
            country (str): Страна производства.
            Возвращает:
            dict: JSON-ответ от API с результатами поиска.
            '''
            headers = {
                        'X-API-KEY': self.__token
                        }
            response = requests.get(self.__url
                                    + f'/movie?page=1&limit=10&type=movie&year={year}&ageRating={age}&countries.name={country}',
                                    headers=headers)
            return response.json()
