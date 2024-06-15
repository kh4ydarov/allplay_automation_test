import pytest
from allure_commons.types import Severity
from allplay_tests.pages.ui.open_page import open_page
import allure


@allure.epic('Section click')
@allure.story('UI Movie section')
@allure.feature('Sections')
@allure.tag('Web')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
@pytest.mark.web
@pytest.mark.critical
@allure.title('Section Movies clickable')
def test_sections_click_tv():
    open_page.open_site()
    open_page.tv_page()
    open_page.asserting_tv_page()


@allure.epic('Section click')
@allure.story('UI Radio section')
@allure.feature('Sections')
@allure.tag('Web')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
@pytest.mark.web
@pytest.mark.critical
@allure.title('Section Radio clickable')
def test_sections_click_radio():
    open_page.open_site()
    open_page.radios_page()
    open_page.asserting_radios_page()
