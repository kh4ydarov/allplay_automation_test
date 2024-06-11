import allure
from allure_commons.types import Severity
from allplay_tests.pages.mobile.search_movies import search


@allure.title('Click search button and search movie')
@allure.tag('mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Search')
@allure.story('Search')
def test_search_movies():
    search.search_movie()
    search.asserting_searching_result()
