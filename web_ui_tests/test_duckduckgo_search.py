import pytest
from web_ui_tests.pages.duckduckgo_page import DuckDuckGoPage

@pytest.mark.parametrize("search_term", [
    "QA automation with Python",
    "Selenium WebDriver tutorial",
    "pytest parameterization example"
])
def test_duckduckgo_search(driver, search_term):
    page = DuckDuckGoPage(driver)
    page.load()
    page.search(search_term)
    page.click_first_result()
    page.wait_for_title_contains(search_term)
