from allure_commons.types import Severity

from allplay_tests.pages.ui.open_page import open_page
from allplay_tests.pages.ui.authorization import authorization
import allure


@allure.title('Authorization with valid data')
@allure.tag('UI')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('User authorization with valid data')
@allure.story('Authorization')
def test_sign_in():
    open_page.open_site()
    open_page.authorization_page()
    open_page.asserting_auth_page()
    authorization.sign_in()
    authorization.assert_sign_in()
