from allplay_tests.pages.search_click import search
from allplay_tests.pages.open_page import open_page


def test_search():
    open_page.open_site()
    search.search_elements()
    search.asserting_result()
