import allure
from allure_commons.types import Severity
from allplay_tests.pages.mobile.search_movies_page import search


@allure.title('Search icon')
@allure.epic('Search icon')
@allure.story('Search movie from icon')
@allure.feature('Search')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity(Severity.NORMAL)
def test_search_movies():
    search.search_movie()
    search.asserting_searching_result()
