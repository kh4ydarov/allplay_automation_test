import allure
from allure_commons.types import Severity
from allplay_tests.pages.mobile.sign_in_page import authorization


@allure.title('Authorization with valid data')
@allure.tag('mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Authorization with valid data')
@allure.story('Authorization')
def test_authorization():
    authorization.mobile_authorization_open_page()
    authorization.fill_username_password()
    authorization.click_submit_button()
