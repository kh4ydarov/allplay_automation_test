import pytest
from allure_commons.types import Severity
from allplay_tests.pages.ui.open_page import open_page
from allplay_tests.pages.ui.authorization import authorization
import allure


@allure.epic('Sign up')
@allure.story('New user registration')
@allure.feature('User registration with valid data')
@allure.tag('Web')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
@pytest.mark.web
@pytest.mark.critical
@allure.title('Registration')
def test_sign_up():
    open_page.open_site()
    open_page.authorization_page()
    open_page.asserting_auth_page()
    authorization.sign_up()
    authorization.asserting_sign_up()
