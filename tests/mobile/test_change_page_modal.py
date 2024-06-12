import allure
from allure_commons.types import Severity
from allplay_tests.pages.mobile.change_page import pages


@allure.title('Modal for change category')
@allure.epic('Category modal window')
@allure.story('Change category from modal window')
@allure.feature('Category modal window')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity(Severity.NORMAL)
def test_change_modal_pages():
    pages.mobile_pages_modal_open()
    pages.asserting_modal_categories()
