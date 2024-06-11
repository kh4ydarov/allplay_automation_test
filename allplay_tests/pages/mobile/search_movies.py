import allure
from selene import browser, command, have, be
from appium.webdriver.common.appiumby import AppiumBy


class Search:
    def search_movie(self):
        with allure.step('Search movie'):
            browser.element((AppiumBy.XPATH,
                             '//android.widget.TextView['
                             '@resource-id="uz.allplay.app:id/navigation_bar_item_small_label_view" and '
                             '@text="Search"]')).click()
            browser.element((AppiumBy.ID, "uz.allplay.app:id/input_view")).type('Terminator')

        with (allure.step('Check the count view text starts with "Found on request: "')):
            browser.element(
                (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="uz.allplay.app:id/count_view"]')).should(
                be.visible)
            return self

    def asserting_searching_result(self):
        with allure.step('Asserting searching results'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="uz.allplay.app:id/count_view"]')
                            ).should(have.text('Found on request: '))

            return self


search = Search()
