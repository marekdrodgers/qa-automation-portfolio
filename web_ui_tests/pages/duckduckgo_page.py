"""
Page object model for DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NoResultsFound(Exception):
    """Exception raised when no search results are found."""


class DuckDuckGoPage:
    """Page object for DuckDuckGo search functionality."""

    URL = "https://duckduckgo.com/"
    SEARCH_INPUT = (By.NAME, "q")
    RESULTS_LINKS = (By.CSS_SELECTOR, "a.result__a")

    def __init__(self, driver):
        """
        Initialize with a Selenium WebDriver instance.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver

    def load(self):
        """Load the DuckDuckGo homepage."""
        self.driver.get(self.URL)

    def search(self, term):
        """
        Perform a search with the given term.

        Args:
            term (str): Search query.
        """
        search_box = self.driver.find_element(*self.SEARCH_INPUT)
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)

    def wait_for_results(self):
        """
        Wait until search results are present.

        Returns:
            list: List of WebElement results.
        """
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.RESULTS_LINKS)
        )

    def click_first_result(self):
        """Click the first search result safely."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.RESULTS_LINKS)
        )
        results = self.driver.find_elements(*self.RESULTS_LINKS)

        if results:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", results[0])
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.RESULTS_LINKS)
            )
            ActionChains(self.driver).move_to_element(results[0]).click().perform()
        else:
            raise NoResultsFound("No search results found.")

    def wait_for_title_contains(self, text):
        """
        Wait until the page title contains the specified text.

        Args:
            text (str): Text expected in the page title.
        """
        WebDriverWait(self.driver, 10).until(
            lambda d: text.lower() in d.title.lower()
        )
