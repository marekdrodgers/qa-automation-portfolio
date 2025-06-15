import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.skip(reason="Google blocks automation via CAPTCHA")
def test_google_search(driver):
    driver.get("https://www.google.com")

    # Wait and click consent if present
    try:
        consent_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "L2AGLb"))
        )
        consent_button.click()
    except:
        pass  # Consent popup not present, proceed

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("QA automation with Python")
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load and verify
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
    )
    assert len(results) > 0
