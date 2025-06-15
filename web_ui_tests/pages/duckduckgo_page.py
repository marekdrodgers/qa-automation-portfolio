from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.result__a"))
        )
        results = self.driver.find_elements(By.CSS_SELECTOR, "a.result__a")

        if results:
            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", results[0])
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.result__a"))
            )
            # Click using ActionChains to avoid overlay issues
            ActionChains(self.driver).move_to_element(results[0]).click().perform()
        else:
            raise Exception("No search results found.")

    def wait_for_title_contains(self, text):
        WebDriverWait(self.driver, 10).until(
            lambda d: text.lower() in d.title.lower()
        )
