"""
Test suite for DuckDuckGo search page functionality.
"""

# pylint: disable=redefined-outer-name
import pytest
from selenium import webdriver
from web_ui_tests.pages.duckduckgo_page import DuckDuckGoPage

@pytest.fixture
def duckduckgo_driver():
    """Initialize and quit the Chrome WebDriver for DuckDuckGo tests."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_duckduckgo_search(duckduckgo_driver):
    """Test that DuckDuckGo search returns results and first result can be clicked."""
    page = DuckDuckGoPage(duckduckgo_driver)
    page.load()
    page.search("Selenium Python")
    page.wait_for_results()
    page.click_first_result()
    page.wait_for_title_contains("Selenium Python")
