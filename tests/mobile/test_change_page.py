import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.title('Change page')
@allure.tag('mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Buttons on start page')
@allure.story('Search movie')
def test_modal_for_change():
    with allure.step('Click for change pages'):
        browser.element((AppiumBy.ID, "android:id/text1")).click()

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
