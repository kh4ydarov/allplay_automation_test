import allure
from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy


class Pages:
    def mobile_pages_modal_open(self):
        with allure.step('Click for change pages'):
            browser.element((AppiumBy.ID, "android:id/text1")).click()
            return self

    def asserting_modal_categories(self):
        with (allure.step('Checking modal for choose page')):
            browser.element((AppiumBy.ID, "uz.allplay.app:id/select_dialog_listview")).should(be.visible)
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1"'
                                             ' and @text="TV"]')
                            ).should(have.text('TV'))
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1"'
                                             ' and @text="Radio"]')
                            ).should(have.text('Radio'))
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1"'
                                             ' and @text="Movies and series"]')
                            ).should(have.text('Movies and series'))
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1"'
                                             ' and @text="GO"]')
                            ).should(have.text('GO'))
            return self

    def change_to_tv_page(self):
        with (allure.step('Change to TV page')):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1"'
                                             ' and @text="TV"]')
                            ).click()
        return self

    def asserting_main_tv_page(self):
        with (allure.step('Asserting tv page')):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1"'
                                             ' and @text="TV"]')
                            ).should(have.text('TV'))
        return self


pages = Pages()
