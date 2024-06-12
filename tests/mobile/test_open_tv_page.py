import allure
from allure_commons.types import Severity
from allplay_tests.pages.mobile.change_page import pages


@allure.epic('Category modal window')
@allure.story('Change category to TV from modal window')
@allure.feature('Category modal window')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity(Severity.NORMAL)
def test_change_to_tv():
    pages.mobile_pages_modal_open()
    pages.asserting_modal_categories()
    pages.change_to_tv_page()
    pages.asserting_main_tv_page()
