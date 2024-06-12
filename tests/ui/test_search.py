from allure_commons.types import Severity

from allplay_tests.pages.ui.search_click import search
from allplay_tests.pages.ui.open_page import open_page
import allure


@allure.title('Search elements')
@allure.tag('Search')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Search')
@allure.story('UI Search button')
def test_search():
    open_page.open_site()
    search.search_elements()
    search.asserting_result()
