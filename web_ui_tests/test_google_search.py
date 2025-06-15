"""
Module for web UI automation testing using Selenium.
This test opens Google and checks if search works correctly.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_google_search():
    """
    Test that verifies Google search returns results for a query.
    """
    # Setup: Start browser
    driver = webdriver.Chrome()

    try:
        # Step 1: Navigate to Google
        driver.get("https://www.google.com")
        time.sleep(1)

        # Step 2: Accept cookies (if present)
        try:
            consent_button = driver.find_element(By.ID, "L2AGLb")
            consent_button.click()
        except Exception:
            pass  # Consent screen not shown

        # Step 3: Enter search term and submit
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("QA automation with Python")
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

        # Step 4: Check that results exist
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        assert len(results) > 0

    finally:
        # Teardown
        driver.quit()
