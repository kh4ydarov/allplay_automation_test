import allure

from selene import browser, be, have, by


class OpenPage:

    def close_promo(self):
        promo_page = browser.element('.PromoPage .ClosePromo').with_(timeout=20).should(be.visible)
        if promo_page.matching(be.visible):
            promo_page.click()
        return self

    def open_site(self):
        with allure.step("Открыть сайт allplay.uz"):
            browser.open("")
            self.close_promo()
            self.close_promo()
            self.close_promo()
        return self

    def tv_page(self):
        with allure.step("Переход в раздел ТВ"):
            browser.element('a.Navbar__link[href="/tv"]').click()
        return self

    def asserting_tv_page(self):
        with allure.step("Проверка страницы после нажатие кнопки в раздел ТВ"):
            browser.element('.PageSection__title-left').should(have.text('Список каналов'))
        return self

    def radios_page(self):
        with allure.step("Переход в раздел Radio"):
            browser.element(by.css('div.Navbar__center')).element(by.xpath('.//a[@href="/radio"]')).click()
        return self

    def asserting_radios_page(self):
        with allure.step("Проверка страницы после нажатие кнопки в раздел Radio"):
            browser.element('.PageSection__title-left').should(have.text('Онлайн-радио'))
        return self

    def authorization_page(self):
        with allure.step("Переход в страницу авторизации"):
            browser.element('a.d-none.d-lg-inline.Navbar__link[href="/login/"]').click()
        return self

    def asserting_auth_page(self):
        with allure.step("Проверка перехода на страницу авторизации после нажатии кнопки Вход"):
            browser.element('.Login__title').should(have.text('Вход'))
        return self


open_page = OpenPage()
