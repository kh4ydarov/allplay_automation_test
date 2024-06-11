import allure

from selene import browser
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
import os

load_dotenv()


class AuthorizationMobile:
    def mobile_authorization_open_page(self):
        with allure.step('Open authorization page'):
            browser.element((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Первый"]')).click()
            browser.element((AppiumBy.ID, 'android:id/button1')).click()
        return self

    def fill_username_password(self):
        with allure.step('Fill username and password'):
            username = os.getenv('user_api_email')
            password = os.getenv('user_api_password')

            browser.element(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="uz.allplay.app:id/email"]')).type(username)

            browser.element(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="uz.allplay.app:id/password"]')).type(password)
            return self

    def click_submit_button(self):
        with allure.step('Click Sign in button'):
            browser.element(
                (AppiumBy.XPATH, '//android.widget.Button[@resource-id="uz.allplay.app:id/submit"]')).click()
        return self


authorization = AuthorizationMobile()
