import pytest
from allure_commons.types import Severity
from allplay_tests.pages.ui.open_page import open_page
import allure


@allure.epic('Section click')
@allure.story('UI Sections')
@allure.feature('Sections')
@allure.tag('Web')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
@pytest.mark.web
@pytest.mark.critical
@allure.title('Search elements')
def test_sections_click():
    open_page.open_site()
    open_page.tv_page()
    open_page.asserting_tv_page()
