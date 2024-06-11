from allplay_tests.pages.ui.open_page import open_page
from allplay_tests.pages.ui.authorization import authorization
import allure


@allure.epic('Authorization with valid data')
@allure.story('Authorization user')
@allure.feature('Authorization')
@allure.tag('Web UI')
@allure.label('Owner')
@allure.severity('High')
def test_sign_in():
    open_page.open_site()
    open_page.authorization_page()
    open_page.asserting_auth_page()
    authorization.sign_in()
    authorization.assert_sign_in()
