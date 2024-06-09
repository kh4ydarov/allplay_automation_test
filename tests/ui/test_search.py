from allplay_tests.pages.search_click import search
from allplay_tests.pages.open_page import open_page
import allure


@allure.epic('Search movie in Web UI')
@allure.story('Search movie')
@allure.feature('Search web ui')
@allure.tag('Web UI')
@allure.label('Owner')
@allure.severity('High')
def test_search():
    open_page.open_site()
    search.search_elements()
    search.asserting_result()
