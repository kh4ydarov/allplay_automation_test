from allplay_tests.pages.open_page import open_page
import allure


@allure.epic('Click sections')
@allure.story('Sections')
@allure.feature('Sections')
@allure.tag('Web UI')
@allure.label('Owner')
@allure.severity('High')
def test_sections_click():
    open_page.open_site()
    open_page.tv_page()
    open_page.asserting_tv_page()
