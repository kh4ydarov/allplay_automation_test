import allure
from allure_commons.types import Severity
from allplay_tests.pages.mobile.sign_in_page import authorization


@allure.epic('Authorization')
@allure.story('Authorization with valid data')
@allure.feature('Authorization')
@allure.tag('mobile')
@allure.label('owner')
@allure.severity(Severity.CRITICAL)
def test_authorization():
    authorization.mobile_authorization_open_page()
    authorization.fill_username_password()
    authorization.click_submit_button()
