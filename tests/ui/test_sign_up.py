from allplay_tests.pages.open_page import open_page
from allplay_tests.pages.authorization import authorization


def test_sign_up():
    open_page.open_site()
    open_page.authorization_page()
    open_page.asserting_auth_page()
    authorization.sign_up()
    authorization.asserting_sign_up()
