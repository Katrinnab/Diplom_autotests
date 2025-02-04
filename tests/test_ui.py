import pytest


# @pytest.mark.skip
def test_enter_page(kino_page):
    kino_page.go_start_page()


def test_search_movie(kino_page):
    kino_page.search_movie("Ландыши")
