import allure

from selene import browser, have


class ChangeLanguage:
    def change_language_uzbek(self):
        with allure.step("Переключение языка пользователя на Узбекский странице в Авторизации"):
            browser.element('.langs [href="/uz/login/"]').click()
        return self

    def asserting_localization_uz(self):
        with allure.step("Проверка локализации после переключение на Узбекский в странице Авторизации"):
            browser.element('.Login__title').should(have.text("Kirish"))
        return self

    def change_language_english(self):
        with allure.step("Переключение языка пользователя на Английский в странице Авторизации"):
            browser.element('.langs [href="/en/login/"]').click()
        return self

    def asserting_localization_eng(self):
        with allure.step("Проверка локализации после переключение на Английский в странице Авторизации"):
            browser.element('.Login__title').should(have.text("Login"))
        return self

    def change_language_russian(self):
        with allure.step("Переключение языка пользователя на Английский в странице Авторизации"):
            browser.element('.langs [href="/en/login/"]').click()
            browser.element('.langs [href="/РУ/login/"]').click()
        return self

    def asserting_localization_russian(self):
        with allure.step("Проверка локализации после переключение на Английский в странице Авторизации"):
            browser.element('.Login__title').should(have.text("Вход"))
        return self


change_language = ChangeLanguage()
