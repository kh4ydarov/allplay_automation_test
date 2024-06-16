import allure

from allplay_tests.test_data.data import user

from selene import browser, command, have, be


class Authorization:
    def sign_up(self):
        with allure.step("Регистрация нового пользователя"):
            browser.element('.Login__link').click()
            browser.element('#referralId').perform(command.js.scroll_into_view).click()
        return self

    def asserting_sign_up_page(self):
        with allure.step("Проверка перехода на страницу регистрации"):
            browser.element('.Login__title').should(have.text('Регистрация'))
        return self

    def sign_in(self):
        with allure.step("Авторизация с валидными данными"):
            browser.element('#email').set_value(user.sign_in_login)
            browser.element('#password').set_value(user.sign_in_password)
            browser.element('.Login__button').click()
        return self

    def assert_sign_in(self):
        with allure.step("Успешная авторизация"):
            if not browser.element('.Alert__text').should(be.visible):
                browser.element('.UserMenu').should(be.visible).should(be.clickable).click()
                browser.element('.UserMenu__avatar').should(be.visible)
        return self


authorization = Authorization()
