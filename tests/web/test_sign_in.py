import pytest
from allure_commons.types import Severity
from allplay_tests.pages.ui.open_page import open_page
from allplay_tests.pages.ui.authorization_page import authorization
import allure


@allure.epic('Authorization')
@allure.story('User authorization')
@allure.feature('User authorization with valid data')
@allure.tag('Web')
@allure.label('owner', 'kh4ydarov')
@allure.severity(Severity.CRITICAL)
@pytest.mark.web
@pytest.mark.critical
@allure.title('Search elements')
def test_sign_in():
    open_page.open_site()
    open_page.authorization_page()
    open_page.asserting_auth_page()
    authorization.sign_in()
    authorization.assert_sign_in()
