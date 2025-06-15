"""
Tests for Google Search using Selenium WebDriver and pytest.
"""
# pylint: disable=redefined-outer-name
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def google_driver():
    """Initialize and quit Chrome WebDriver for Google tests."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.skip(reason="Google blocks automation via CAPTCHA")
def test_google_search(google_driver):
    """Search on Google and verify results appear."""
    driver = google_driver
    driver.get("https://www.google.com")

    try:
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "L2AGLb"))
        )
        consent_button.click()
    except TimeoutException:
        # Consent popup didn't appear; continue
        pass

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("OpenAI")
    search_box.submit()

    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#search a"))
    )
    assert len(results) > 0, "No search results found!"
