import pytest


# @pytest.mark.skip
def test_search_id(main_page):
    movie = main_page.search_for_id(935898)
    assert movie['id'] == 935898


# @pytest.mark.skip
def test_by_name(main_page):
    movie = main_page.search_by_name("Титаник")
    assert "Титаник".lower() in movie['docs'][0]['name'].lower()


# @pytest.mark.skip
def test_by_type(main_page):
    movie = main_page.search_by_type("cartoon")
    assert movie['docs'][4]['type'] == "cartoon"


# @pytest.mark.skip
def test_by_feature_date(main_page):
    movie = main_page.search_by_feature_date(2100)
    assert movie['error'] == 'Bad Request'


# @pytest.mark.skip
def test_by_year_and_genre(main_page):
    movie = main_page.search_by_year_and_genres(2022, "комедия")
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

    assert is_find_year is True
    assert is_find_genre is True


# @pytest.mark.skip
def test_by_invalid_rating(main_page):
    movie = main_page.search_by_invalid_rating(13)
    assert movie['error'] == 'Bad Request'


# @pytest.mark.skip
def test_by_year_age_country(main_page):
    movie = main_page.search_by_year_age_country(2022, 18, "Россия")
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

    assert is_find_year is True
    assert is_find_age is True
    assert is_find_countries is True
