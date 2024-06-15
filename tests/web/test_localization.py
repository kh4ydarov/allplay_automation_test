import pytest
from allure_commons.types import Severity
from allplay_tests.pages.ui.change_language_page import change_language
from allplay_tests.pages.ui.open_page import open_page
import allure


@allure.epic('Login')
@allure.story('UI Localization')
@allure.feature('Localization')
@allure.tag('web')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
@pytest.mark.web
@pytest.mark.critical
@allure.title('Change language to uzbek')
def test_change_language_uz():
    open_page.open_site()
    open_page.authorization_page()
    change_language.change_language_uzbek()
    change_language.asserting_localization_uz()


@allure.epic('Login')
@allure.story('UI Localization')
@allure.feature('Localization')
@allure.tag('web')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
@pytest.mark.web
@pytest.mark.critical
@allure.title('Change language to english')
def test_change_language_en():
    open_page.open_site()
    open_page.authorization_page()
    change_language.change_language_english()
    change_language.asserting_localization_eng()
