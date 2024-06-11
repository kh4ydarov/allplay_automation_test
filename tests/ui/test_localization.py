from allplay_tests.pages.ui.change_language import change_language
from allplay_tests.pages.ui.open_page import open_page
import allure


@allure.epic('Change language to uzbek')
@allure.story('Localization')
@allure.feature('Localization')
@allure.tag('Web UI')
@allure.label('Owner')
@allure.severity('High')
def test_change_language_uz():
    open_page.open_site()
    open_page.authorization_page()
    change_language.change_language_uzbek()
    change_language.asserting_localization_uz()


@allure.epic('Change language to English')
@allure.story('Localization')
@allure.feature('Localization')
@allure.tag('Web UI')
@allure.label('Owner')
@allure.severity('High')
def test_change_language_en():
    open_page.open_site()
    open_page.authorization_page()
    change_language.change_language_english()
    change_language.asserting_localization_eng()
