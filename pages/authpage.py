import requests


class AuthPage:
    def __init__(self, token):
        self.__url = 'https://api.kinopoisk.dev/v1.4'
        self.__token = token

    def search_for_id(self, id):
        headers = {
                    'X-API-KEY': self.__token
                    }
        response = requests.get(self.__url + f'/movie/{str(id)}',
                                headers=headers)
        return response.json()

    def search_by_name(self, name):
        headers = {
                    'X-API-KEY': self.__token
                    }
        response = requests.get(self.__url +
                                f'/movie/search?page=1&limit=10&query={name}',
                                headers=headers)
        return response.json()

    def search_by_type(self, type):
        headers = {
                    'X-API-KEY': self.__token
                    }
        response = requests.get(self.__url +
                                f'/movie?page=1&limit=10&type={type}',
                                headers=headers)
        return response.json()

    def search_by_feature_date(self, date):
        headers = {
                    'X-API-KEY': self.__token
                    }
        response = requests.get(self.__url + f'/movie?year={date}',
                                headers=headers)
        return response.json()

    def search_by_year_and_genres(self, year, genre):
        headers = {
                    'X-API-KEY': self.__token
                    }
        response = requests.get(self.__url + f'/movie?year={year}&genres.name={genre}',
                                headers=headers)
        return response.json()

    def search_by_invalid_rating(self, rating):
        headers = {
                    'X-API-KEY': self.__token
                    }
        response = requests.get(self.__url + f'/movie?rating.imdb={rating}',
                                headers=headers)
        return response.json()

    def search_by_year_age_country(self, year, age, country):
        headers = {
                    'X-API-KEY': self.__token
                    }
        response = requests.get(self.__url
                                + f'/movie?page=1&limit=10&type=movie&year={year}&ageRating={age}&countries.name={country}',
                                headers=headers)
        return response.json()
