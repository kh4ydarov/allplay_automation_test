import pytest
from allure_commons.types import Severity
from allplay_tests.pages.ui.open_page import open_page
from allplay_tests.pages.ui.authorization_page import authorization
import allure


@allure.epic('Sign up page for new users')
@allure.story('New user registration page')
@allure.feature('User registration page')
@allure.tag('Web')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
@pytest.mark.web
@pytest.mark.critical
@allure.title('Registration page')
def test_sign_up():
    open_page.open_site()
    open_page.authorization_page()
    open_page.asserting_auth_page()
    authorization.sign_up()
    authorization.asserting_sign_up_page()
