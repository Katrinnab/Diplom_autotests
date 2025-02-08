import pytest
import allure

'''
Этот файл содержит тесты для проверки функциональности API Кинопоиска.
Тесты используют фикстуру main_page, которая предоставляет доступ к методам
класса AuthPage из файла authpage.py.
'''


@allure.title("Тест сравнения id фильма")
@allure.description("Сравниваем вернувшийся результат с id от сайта и заданный")
@allure.feature("Проверяем поле id на заданное значение")
@allure.severity(allure.severity_level.NORMAL)
def test_search_id(main_page):
    '''
    Описание: Проверяет, что поиск фильма по ID возвращает корректный фильм.
    Параметры:
    main_page: Фикстура, предоставляющая доступ к методам API.
    Проверка:
    Убеждается, что ID фильма в ответе соответствует запрошенному ID (935898).
        '''
    with allure.step("Посылаем значение id для поиска на сайте"):
        movie = main_page.search_for_id(935898)
    with allure.step("Сравниваем результат ответа сайта"):
        assert movie['id'] == 935898


@allure.title("Тест сравнения наименований фильма")
@allure.description("Сравниваем вернувшийся результат с названием фильма и заданный")
@allure.feature("Сверяем вернувшееся название с заданным")
@allure.severity(allure.severity_level.NORMAL)
def test_by_name(main_page):
    '''
    Описание: Проверяет, что поиск фильма по названию возвращает корректный результат.
    Параметры:
    main_page: Фикстура, предоставляющая доступ к методам API.
    Проверка:
    Убеждается, что название фильма "Титаник" содержится в ответе.
    '''
    with allure.step("Посылаем название фильма для поиска на сайте"):
        movie = main_page.search_by_name("Титаник")
    with allure.step("Сравниваем результат ответа сайта"):
        assert "Титаник".lower() in movie['docs'][0]['name'].lower()


@allure.title("Тест сравнения типов фильма")
@allure.description("Сравниваем вернувшийся результат с типом фильма и заданный")
@allure.feature("Сверяем вернувшейся тип с заданным")
@allure.severity(allure.severity_level.NORMAL)
def test_by_type(main_page):
    '''
    Описание: Проверяет, что поиск фильмов по типу (например, мультфильм) возвращает корректный результат.
    Параметры:
    main_page: Фикстура, предоставляющая доступ к методам API.
    Проверка:
    Убеждается, что тип фильма в ответе соответствует запрошенному типу ("cartoon").
    '''
    with allure.step("Посылаем тип фильма для поиска на сайте"):
        movie = main_page.search_by_type("cartoon")
    with allure.step("Сравниваем результат ответа сайта"):
        assert movie['docs'][4]['type'] == "cartoon"


@allure.title("Негативный тест на проверку поведения сайта при задании некорректного значения года выпуска фильма")
@allure.description("Сравниваем статус ответа сайта с ожидаемым")
@allure.feature("Сверяем вернувшейся статус ответа")
@allure.severity(allure.severity_level.NORMAL)
def test_by_feature_date(main_page):
    '''
    Описание: Проверяет, что поиск фильмов по несуществующему году (2100) возвращает ошибку.
    Параметры:
    main_page: Фикстура, предоставляющая доступ к методам API.
    Проверка:
    Убеждается, что ответ содержит ошибку "Bad Request".
    '''
    with allure.step("Посылаем в запросе невалидное значение года выпуска"):
        movie = main_page.search_by_feature_date(2100)
    with allure.step("Сравниваем результат ответа сайтас ожидаемым"):
        assert movie['error'] == 'Bad Request'


@allure.title("Тест на поиск фильма по заданным критериям - жанр и год выпуска")
@allure.description("Сравниваем результат ответа сайта с заданными параметрами")
@allure.feature("Сверяем вернувшиеся данные")
@allure.severity(allure.severity_level.NORMAL)
def test_by_year_and_genre(main_page):
    '''
    Описание: Проверяет, что поиск фильмов по году и жанру возвращает корректные результаты.
    Параметры:
    main_page: Фикстура, предоставляющая доступ к методам API.
    Проверка:
    Убеждается, что все фильмы в ответе соответствуют указанному году (2022) и жанру ("комедия").
    '''
    with allure.step("Посылаем в запросе конкретные значения для поиска"):
        movie = main_page.search_by_year_and_genres(2022, "комедия")
    with allure.step("Проверяем найденные значения"):
        # Есть ли неправильный год в списке фильмов
        is_find_year = True
        is_find_genre = True
    for dct in movie['docs']:
        if dct.get("year", '') != 2022:
            is_find_year = False
            break

        lst_genres = dct.get("genres", [])
        if lst_genres == []:
            is_find_genre = False
            break

        is_find_genre = False
        for dct_genres in lst_genres:
            if dct_genres.get("name", '') == "комедия":
                is_find_genre = True
                break

        if not is_find_genre:
            break

    with allure.step("Сравниваем полученные значения на сайте"):
        assert is_find_year is True
        assert is_find_genre is True


@allure.title("Негативный тест на проверку поведения сайта при некорректном отправленном значении рейтинга")
@allure.description("Сравниваем статус ответа с сайта с ожидаемым")
@allure.feature("Сверяем вернувшийся статус ответа")
@allure.severity(allure.severity_level.NORMAL)
def test_by_invalid_rating(main_page):
    '''
    Описание: Проверяет, что поиск фильмов по недопустимому рейтингу (13) возвращает ошибку.
    Параметры:
    main_page: Фикстура, предоставляющая доступ к методам API.
    Проверка:
    Убеждается, что ответ содержит ошибку "Bad Request".
    '''
    with allure.step("Посылаем в запросе невалидное значение для поиска"):
        movie = main_page.search_by_invalid_rating(13)
    with allure.step("Сравниваем статус ответа с ожидаемым"):
        assert movie['error'] == 'Bad Request'


@allure.title("Тест на поиск фильма по заданным критериям - год выпуска, возраст и страну производства")
@allure.description("Сравниваем результат ответа сайта с заданными параметрами")
@allure.feature("Сверяем вернувшиеся данные")
@allure.severity(allure.severity_level.NORMAL)
def test_by_year_age_country(main_page):
    '''
    Описание: Проверяет, что поиск фильмов по году, возрастному рейтингу и стране возвращает корректные результаты.
    Параметры:
    main_page: Фикстура, предоставляющая доступ к методам API.
    Проверка:
    Убеждается, что все фильмы в ответе соответствуют указанному году (2022), возрастному рейтингу (18) и стране ("Россия").
    '''
    with allure.step("Посылаем в запросе конкретные значения для поиска"):
        movie = main_page.search_by_year_age_country(2022, 18, "Россия")
    with allure.step("Проверяем найденные значения"):
        # Есть ли неправильный год в списке фильмов
        is_find_year = True
        is_find_countries = True
        is_find_age = True

    for dct in movie['docs']:
        if dct.get("year", '') != 2022:
            is_find_year = False
            break

        if dct.get("ageRating", 0) != 18:
            is_find_age = False
            break

        lst_countries = dct.get("countries", [])
        if lst_countries == []:
            is_find_countries = False
            break

        is_find_countries = False
        for dct_countries in lst_countries:
            if dct_countries.get("name", '') == "Россия":
                is_find_countries = True
                break

        if not is_find_countries:
            break
    with allure.step("Сравниваем полученные значения на сайте"):
        assert is_find_year is True
        assert is_find_age is True
        assert is_find_countries is True
