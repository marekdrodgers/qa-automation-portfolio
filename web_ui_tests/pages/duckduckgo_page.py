from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoPage:
    URL = "https://duckduckgo.com/"
    SEARCH_INPUT = (By.NAME, "q")
    RESULTS_LINKS = (By.CSS_SELECTOR, "a.result__a")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, term):
        search_box = self.driver.find_element(*self.SEARCH_INPUT)
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)

    def wait_for_results(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.RESULTS_LINKS)
        )

    def click_first_result(self):
        results = self.wait_for_results()
        results[0].click()

    def wait_for_title_contains(self, text):
        WebDriverWait(self.driver, 10).until(
            lambda d: text.lower() in d.title.lower()
        )
