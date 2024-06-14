import pytest
from allure_commons.types import Severity
from allplay_tests.pages.ui.search_click_page import search
from allplay_tests.pages.ui.open_page import open_page
import allure


@allure.epic('Search')
@allure.story('UI Search button')
@allure.feature('Search')
@allure.tag('web')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
@pytest.mark.web
@pytest.mark.critical
@allure.title('Search elements')
def test_search():
    open_page.open_site()
    search.search_elements()
    search.asserting_result()
