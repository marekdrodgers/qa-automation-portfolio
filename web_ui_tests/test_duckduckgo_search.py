from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_duckduckgo_search(driver):
    """Test that a DuckDuckGo search leads to a relevant page."""
    driver.get("https://duckduckgo.com/")

    # Enter search term
    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("QA automation with Python")
    search_input.send_keys(Keys.RETURN)

    # Wait for results
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.result__a"))
    )

    assert len(results) > 0, "No results found"

    # Click the first result
    results[0].click()

    # Wait for page title to reflect result
    WebDriverWait(driver, 10).until(
        lambda d: "qa automation" in d.title.lower()
    )
