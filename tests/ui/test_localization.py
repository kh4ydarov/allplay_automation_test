from allure_commons.types import Severity

from allplay_tests.pages.ui.change_language import change_language
from allplay_tests.pages.ui.open_page import open_page
import allure


@allure.title('Change language to uzbek')
@allure.tag('Localization')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Localization')
@allure.story('UI Localization')
def test_change_language_uz():
    open_page.open_site()
    open_page.authorization_page()
    change_language.change_language_uzbek()
    change_language.asserting_localization_uz()


@allure.title('Change language to english')
@allure.tag('Localization')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Localization')
@allure.story('UI Localization')
def test_change_language_en():
    open_page.open_site()
    open_page.authorization_page()
    change_language.change_language_english()
    change_language.asserting_localization_eng()
