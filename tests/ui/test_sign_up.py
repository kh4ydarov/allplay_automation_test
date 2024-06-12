from allure_commons.types import Severity

from allplay_tests.pages.ui.open_page import open_page
from allplay_tests.pages.ui.authorization import authorization
import allure


@allure.title('New user registration with valid data')
@allure.tag('UI Registration')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('User registration with valid data')
@allure.story('Registration')
def test_sign_up():
    open_page.open_site()
    open_page.authorization_page()
    open_page.asserting_auth_page()
    authorization.sign_up()
    authorization.asserting_sign_up()
