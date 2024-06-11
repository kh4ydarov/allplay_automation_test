import allure
from allure_commons.types import Severity
from allplay_tests.pages.mobile.change_page import pages


@allure.title('Change page to TV')
@allure.tag('mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Change page modal')
@allure.story('TV page')
def test_change_to_tv():
    pages.mobile_pages_modal_open()
    pages.asserting_modal_categories()
    pages.change_to_tv_page()
    pages.asserting_main_tv_page()