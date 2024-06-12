import allure
from allure_commons.types import Severity
from allplay_tests.pages.mobile.change_page import pages


@allure.title('Change page modal')
@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Opening changing page modal')
@allure.story('Change page')
def test_change_modal_pages():
    pages.mobile_pages_modal_open()
    pages.asserting_modal_categories()
