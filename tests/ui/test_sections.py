from allure_commons.types import Severity

from allplay_tests.pages.ui.open_page import open_page
import allure


@allure.title('Section click')
@allure.tag('Sections')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'kh4ydarov')
@allure.feature('Section')
@allure.story('UI Section')
def test_sections_click():
    open_page.open_site()
    open_page.tv_page()
    open_page.asserting_tv_page()
